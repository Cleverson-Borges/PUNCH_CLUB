from Entidades.boxeador import Boxeador
from Entidades.caracteristica import Caracteristica
from Telas.tela_caracteristica import TelaCaracteristica
from Telas.tela_boxeador import TelaBoxeador
from DAOs.boxeador_dao import BoxeadorDAO


# Lutadores controlados pela CPU: (nome, apelido, idade, peso, altura, nacionalidade, cpf, nível)
BOXEADORES_CPU = [
    ('Tony Tucker', 'Tucker', 30, 100, 1.90, 'EUA', 128756789, 'facil'),
    ('John Ruiz', 'Ruiz', 33, 75, 1.81, 'EUA', 122456129, 'medio'),
    ('Mike Tyson', 'Tyson', 30, 100, 1.90, 'EUA', 123456555, 'dificil'),
    ('Fabiano Pena', 'Pena', 24, 76, 1.78, 'BRA', 123454321, 'facil'),
    ('Jorge Silva', 'Silva', 33, 75, 1.81, 'BRA', 123156789, 'medio'),
    ('Jean Hauck', 'GOAT', 18, 135, 2.23, 'UFSC', 121756789, 'dificil'),
    ('Anderson Popó', 'Popó', 35, 80, 1.87, 'Brasil', 123436749, 'dificil'),
    ('Rocky Balboa', 'Garanhão Italiano', 30, 82, 1.78, 'EUA', 130000001, 'medio'),
    ('Apollo Creed', 'Mestre do Desastre', 32, 86, 1.88, 'EUA', 130000002, 'dificil'),
    ('Ivan Drago', 'Drago', 28, 118, 1.96, 'URS', 130000003, 'dificil'),
    ('Clubber Lang', 'Clubber', 29, 92, 1.83, 'EUA', 130000004, 'medio'),
    ('Tyler Durden', 'Durden', 31, 78, 1.83, 'EUA', 130000005, 'medio'),
    ('Billy Hope', 'The Great', 34, 79, 1.80, 'EUA', 130000006, 'facil'),
    ('Maggie Fitzgerald', 'Mo Cuishle', 31, 61, 1.70, 'EUA', 130000007, 'facil'),
    ('Tommy Conlon', 'Riordan', 27, 88, 1.85, 'EUA', 130000008, 'facil'),
]

CARACTERISTICAS_CPU = {
    'facil': {'forca': 10, 'esquiva': 10, 'vida': 100, 'defesa': 10, 'stamina': 10},
    'medio': {'forca': 10, 'esquiva': 12, 'vida': 125, 'defesa': 13, 'stamina': 12},
    'dificil': {'forca': 12, 'esquiva': 15, 'vida': 150, 'defesa': 15, 'stamina': 15},
}

PONTOS_POR_VITORIA = 5


class ControladorBoxeador:
    def __init__(self, controlador_central):
        self.__tela_boxeador = TelaBoxeador()
        self.__tela_caracteristica = TelaCaracteristica()
        self.__controlador_central = controlador_central
        self.__boxeador_dao = BoxeadorDAO()
        self.gerar_boxeador()

    @property
    def boxeadores(self):
        return self.__boxeador_dao.get_all()

    def busca_por_cpf(self, cpf):
        # Busca um usuário na lista de boxeadors com base no CPF
        for boxeador in self.__boxeador_dao.get_all():
            if(boxeador.cpf == cpf):
                return boxeador
        return None

    def proximo_numero_inscricao(self):
        numeros = [boxeador.numero_inscricao for boxeador in self.__boxeador_dao.get_all()]
        return max(numeros, default=0) + 1

    def cadastrar_boxeador(self):
        cpf = self.__tela_boxeador.obtem_cpf()
        if cpf is None:
            return
        if self.busca_por_cpf(cpf) is not None:
            self.__tela_boxeador.mostrar_mensagem("CPF já cadastrado.")
            return

        dicionario_informacoes_boxeador = self.__tela_boxeador.cadastrar_boxeador()
        if dicionario_informacoes_boxeador is None:
            return
        dicionario_informacoes_caracteristica = self.cadastrar_caracteristicas()
        if dicionario_informacoes_caracteristica is None:
            self.__tela_boxeador.mostrar_mensagem("Cadastro cancelado.")
            return
        lista_habilidades_escolhidas = self.escolher_habilidades()
        if lista_habilidades_escolhidas is None:
            self.__tela_boxeador.mostrar_mensagem("Cadastro cancelado.")
            return

        caracteristicas_boxeador = Caracteristica(**dicionario_informacoes_caracteristica)
        boxeador = Boxeador(
            nome=dicionario_informacoes_boxeador['nome'],
            apelido=dicionario_informacoes_boxeador['apelido'],
            idade=dicionario_informacoes_boxeador['idade'],
            peso=dicionario_informacoes_boxeador['peso'],
            altura=dicionario_informacoes_boxeador['altura'],
            nacionalidade=dicionario_informacoes_boxeador['nacionalidade'],
            cpf=cpf,
            caracteristica=caracteristicas_boxeador,
            boxeador_cpu=False,
            numero_inscricao=self.proximo_numero_inscricao()
        )
        boxeador.habilidades.extend(lista_habilidades_escolhidas)

        self.__boxeador_dao.add(boxeador)
        self.__tela_boxeador.mostrar_mensagem('Boxeador cadastrado com sucesso!')

    def gerar_boxeador(self):
        # Garante que todos os boxeadores da CPU existam (inclusive em bases salvas por versões antigas).
        for nome, apelido, idade, peso, altura, nacionalidade, cpf, nivel in BOXEADORES_CPU:
            if self.busca_por_cpf(cpf) is not None:
                continue
            boxeador = Boxeador(
                nome=nome,
                apelido=apelido,
                idade=idade,
                peso=peso,
                altura=altura,
                nacionalidade=nacionalidade,
                cpf=cpf,
                caracteristica=Caracteristica(**CARACTERISTICAS_CPU[nivel]),
                boxeador_cpu=True,
                numero_inscricao=self.proximo_numero_inscricao()
            )
            self.__boxeador_dao.add(boxeador)

    def dados_boxeador(self, boxeador):
        return {'nome': boxeador.nome,
                'cpf': boxeador.cpf,
                'apelido': boxeador.apelido,
                'idade': boxeador.idade,
                'peso': boxeador.peso,
                'altura': boxeador.altura,
                'nacionalidade': boxeador.nacionalidade,
                'numero_inscricao': boxeador.numero_inscricao,
                'CPU': boxeador.boxeador_cpu}

    def listar_boxeadores(self):
        if not self.__boxeador_dao.is_empty():
            boxeadores_cadastrados = [self.dados_boxeador(boxeador) for boxeador in self.__boxeador_dao.get_all()]
            self.__tela_boxeador.mostra_boxeador(boxeadores_cadastrados)
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador cadastrado!")

    def listar_boxeadores_edicao_exclusao(self):
        # Lista apenas os boxeadores do usuário (os da CPU não podem ser editados)
        if not self.boxeador_dao_usuario_is_empty():
            boxeadores_usuarios_cadastrados = [self.dados_boxeador(boxeador) for boxeador in self.boxeadores_usuario()]
            self.__tela_boxeador.mostra_boxeador(boxeadores_usuarios_cadastrados)
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador de usuário cadastrado!")

    def seleciona_boxeador_usuario(self, mensagem=None):
        # Mostra os boxeadores do usuário e pede um CPF. Retorna o boxeador ou None.
        if self.boxeador_dao_usuario_is_empty():
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador de usuário cadastrado!")
            return None
        self.listar_boxeadores_edicao_exclusao()
        if mensagem:
            self.__tela_boxeador.mostrar_mensagem(mensagem)
        cpf = self.__tela_boxeador.obtem_cpf()
        if cpf is None:
            return None
        boxeador = self.busca_por_cpf(cpf)
        if boxeador is None or boxeador.boxeador_cpu:
            self.__tela_boxeador.mostrar_mensagem("CUIDADO: ESTE BOXEADOR NÃO EXISTE!")
            return None
        return boxeador

    def listar_habilidade_boxeador(self):
        boxeador = self.seleciona_boxeador_usuario()
        if boxeador is None:
            return
        lista_habilidades_boxeador = []
        for habilidade in boxeador.habilidades:
            dados = {'id': habilidade.id,
                     'nome': habilidade.nome,
                     'descricao': habilidade.descricao,
                     'custo': habilidade.custo,
                     'tipo': habilidade.tipo}
            if habilidade.tipo == 'Ataque':
                dados['dano'] = habilidade.dano
            elif habilidade.tipo == 'Defesa':
                dados['taxa_defesa'] = habilidade.taxa_defesa
            elif habilidade.tipo == 'Esquiva':
                dados['taxa_esquiva'] = habilidade.taxa_esquiva
            lista_habilidades_boxeador.append(dados)
        self.__tela_boxeador.lista_habilidades(lista_habilidades_boxeador)

    def listar_caracteristica_boxeador(self):
        boxeador = self.seleciona_boxeador_usuario()
        if boxeador is None:
            return
        bonus = self.bonificacao_por_peso(boxeador)
        descricao_bonus = ', '.join(f'{nome} {valor:+d}' for nome, valor in bonus.items() if valor != 0)
        self.__tela_boxeador.mostrar_caracteristica_boxeador([{
            'forca': boxeador.caracteristica.forca,
            'esquiva': boxeador.caracteristica.esquiva,
            'vida': boxeador.caracteristica.vida,
            'defesa': boxeador.caracteristica.defesa,
            'stamina': boxeador.caracteristica.stamina,
            'imc': self.calcula_imc(boxeador),
            'bonus_imc': descricao_bonus or 'sem alterações'}])

    def alterar_boxeador(self):
        boxeador = self.seleciona_boxeador_usuario("Insira o CPF do boxeador que deseja alterar")
        if boxeador is None:
            return
        self.__tela_boxeador.mostrar_mensagem("Insira os novos dados do boxeador")
        novos_dados = self.__tela_boxeador.cadastrar_boxeador()
        if novos_dados is None:
            return
        boxeador.nome = novos_dados["nome"]
        boxeador.apelido = novos_dados["apelido"]
        boxeador.idade = novos_dados["idade"]
        boxeador.peso = novos_dados["peso"]
        boxeador.altura = novos_dados["altura"]
        boxeador.nacionalidade = novos_dados["nacionalidade"]

        if self.__tela_boxeador.confirmar("Deseja redistribuir os pontos de características?\n"
                                          "(os pontos ganhos em torneios serão perdidos)"):
            nova_caracteristica = self.cadastrar_caracteristicas()
            if nova_caracteristica is not None:
                boxeador.caracteristica = Caracteristica(**nova_caracteristica)
        if self.__tela_boxeador.confirmar("Deseja escolher novas habilidades?"):
            novas_habilidades = self.escolher_habilidades()
            if novas_habilidades is not None:
                boxeador.habilidades.clear()
                boxeador.habilidades.extend(novas_habilidades)

        self.__boxeador_dao.update(boxeador)
        self.__tela_boxeador.mostrar_mensagem("Boxeador alterado com sucesso!")

    def excluir_boxeador(self):
        usuario = self.seleciona_boxeador_usuario("Insira o CPF do boxeador que deseja excluir")
        if usuario is None:
            return
        self.__boxeador_dao.remove(usuario)
        self.__controlador_central.controlador_torneio.remover_torneio_por_usuario(usuario)
        self.__tela_boxeador.mostrar_mensagem("Boxeador excluído com sucesso!")

    def cadastrar_caracteristicas(self):
        return self.__tela_caracteristica.tela_cadastro_status()

    def distribuir_pontos_vitoria(self, boxeador):
        # Regra da documentação: cada luta vencida no torneio dá 5 pontos de característica.
        self.__tela_boxeador.mostrar_mensagem(f"Vitória! Você ganhou {PONTOS_POR_VITORIA} pontos para "
                                              f"distribuir nas características de {boxeador.apelido}.")
        caracteristica = boxeador.caracteristica
        valores_atuais = {'forca': caracteristica.forca, 'esquiva': caracteristica.esquiva,
                          'vida': caracteristica.vida, 'defesa': caracteristica.defesa,
                          'stamina': caracteristica.stamina}
        novos_valores = self.__tela_caracteristica.tela_distribuir_pontos(PONTOS_POR_VITORIA, valores_atuais)
        caracteristica.forca = novos_valores['forca']
        caracteristica.esquiva = novos_valores['esquiva']
        caracteristica.vida = novos_valores['vida']
        caracteristica.defesa = novos_valores['defesa']
        caracteristica.stamina = novos_valores['stamina']
        self.__boxeador_dao.update(boxeador)

    def escolher_habilidades(self):
        return self.__controlador_central.controlador_habilidade.adicionar_habilidade()

    def listar_caracteristicas(self, boxeador:Boxeador):
        return boxeador.caracteristica

    def verifica_jogadores_maquina(self):
        # Retorna True se existe pelo menos um boxeador controlado pelo usuário.
        if self.boxeador_dao_usuario_is_empty():
            self.__tela_boxeador.mostrar_mensagem("Não é possível iniciar o jogo, você tem que controlar 1 jogador!")
            self.__tela_boxeador.mostrar_mensagem("Por favor, cadastre um boxeador antes")
            return False
        return True

    def calcula_imc(self, boxeador):
        return boxeador.peso / (boxeador.altura * boxeador.altura)

    def bonificacao_por_peso(self, boxeador):
        # Ajustes de força, esquiva e stamina conforme o IMC (regra da documentação).
        # Não altera o boxeador: o bônus é aplicado só durante as lutas.
        imc = self.calcula_imc(boxeador)
        if imc < 17:
            return {'forca': -5, 'esquiva': 7, 'stamina': 5}
        elif imc < 18.5:
            return {'forca': -2, 'esquiva': 5, 'stamina': 3}
        elif imc < 30:
            return {'forca': 0, 'esquiva': 0, 'stamina': 0}
        elif imc < 35:
            return {'forca': 2, 'esquiva': -3, 'stamina': -2}
        else:
            return {'forca': 5, 'esquiva': -5, 'stamina': -4}

    def caracteristicas_de_luta(self, boxeador):
        # Características efetivas usadas na luta: base do boxeador + bônus do IMC.
        bonus = self.bonificacao_por_peso(boxeador)
        caracteristica = boxeador.caracteristica
        return {'forca': max(1, caracteristica.forca + bonus['forca']),
                'esquiva': max(0, caracteristica.esquiva + bonus['esquiva']),
                'vida': caracteristica.vida,
                'defesa': caracteristica.defesa,
                'stamina': max(1, caracteristica.stamina + bonus['stamina'])}

    def abre_tela(self):
        escolha_tela = {1: self.cadastrar_boxeador,
                        2: self.alterar_boxeador,
                        3: self.listar_boxeadores,
                        4: self.excluir_boxeador,
                        5: self.listar_habilidade_boxeador,
                        6: self.listar_caracteristica_boxeador}

        while True:
            opcao = self.__tela_boxeador.primeira_tela_opcoes()
            if opcao == 0:
                return
            escolha_tela[opcao]()

    def retornar_boxeadores_cpu(self):
        return [boxeador for boxeador in self.__boxeador_dao.get_all() if boxeador.boxeador_cpu is True]

    def boxeadores_usuario(self):
        return [boxeador for boxeador in self.__boxeador_dao.get_all() if boxeador.boxeador_cpu is False]

    def boxeador_dao_usuario_is_empty(self):
        return len(self.boxeadores_usuario()) == 0
