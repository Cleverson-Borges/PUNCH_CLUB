from Entidades.boxeador import Boxeador
from Entidades.caracteristica import Caracteristica
from Telas.tela_caracteristica import TelaCaracteristica
from Telas.tela_boxeador import TelaBoxeador
from DAOs.boxeador_dao import BoxeadorDAO


class ControladorBoxeador:
    def __init__(self, controlador_central):
        self.__tela_boxeador = TelaBoxeador()
        self.__tela_caracteristica = TelaCaracteristica()
        self.__controlador_central = controlador_central
        self.__boxeador_dao = BoxeadorDAO()
        self.__numero_inscricao = 1
        if len(self.__boxeador_dao.get_all()) > 0:
            self.gerar_boxeador()

    @property
    def boxeadores(self):
        return self.__boxeador_dao.get_all()

    def le_str_valida(self, mensagem="", strs_validas=None):
        while True:
            valor_lido = input(mensagem)
            if strs_validas and valor_lido not in strs_validas:
                print("Valor inválido!")
                if strs_validas:
                    print("Valores válidos: ", ", ".join(strs_validas))
            else:
                return valor_lido

    def busca_por_cpf(self, cpf):
        # Busca um usuário na lista de boxeadors com base no CPF
        for boxeador in self.__boxeador_dao.get_all():
            if(boxeador.cpf == cpf):
                return boxeador
        return None

    def cadastrar_boxeador(self):
        cpf = self.__tela_boxeador.obtem_cpf()
        try:
            if self.busca_por_cpf(cpf) is not None:
                raise ValueError("CPF já cadastrado.")
        except ValueError as e:
            print(e)  # Ou realize qualquer outra ação de tratamento necessária.
        else:
            dicionario_informacoes_boxeador = self.__tela_boxeador.cadastrar_boxeador()
            dicionario_informacoes_boxeador['cpf'] = cpf
            dicionario_informacoes_caracteristica = self.cadastrar_caracteristicas()
            boxeador_cpu = False

            # caracteristica_exemplo = Caracteristica(
            #     forca=10,
            #     esquiva=10,
            #     vida=100,
            #     defesa=10,
            #     stamina=10,
            # )
            #
            # boxeador = Boxeador(
            #     nome='Exemplo',
            #     apelido='Exemplo',
            #     idade=10,
            #     peso=10,
            #     altura=10,
            #     nacionalidade='Exemplo',
            #     cpf=123456789,
            #     caracteristica=caracteristica_exemplo,
            #     boxeador_cpu=False,
            #     numero_inscricao=0
            # )

            caracteristicas_boxeador = Caracteristica(
                forca=dicionario_informacoes_caracteristica['forca'],
                esquiva=dicionario_informacoes_caracteristica['esquiva'],
                vida=dicionario_informacoes_caracteristica['vida'],
                defesa=dicionario_informacoes_caracteristica['defesa'],
                stamina=dicionario_informacoes_caracteristica['stamina'],
            )

            boxeador = Boxeador(
                nome=dicionario_informacoes_boxeador['nome'],
                apelido=dicionario_informacoes_boxeador['apelido'],
                idade=dicionario_informacoes_boxeador['idade'],
                peso=dicionario_informacoes_boxeador['peso'],
                altura=dicionario_informacoes_boxeador['altura'],
                nacionalidade=dicionario_informacoes_boxeador['nacionalidade'],
                cpf=dicionario_informacoes_boxeador['cpf'],
                caracteristica=caracteristicas_boxeador,
                boxeador_cpu=boxeador_cpu,
                numero_inscricao=self.__numero_inscricao
            )
            lista_habilidades_escolhidas = self.escolher_habilidades()
            if lista_habilidades_escolhidas is None and len(boxeador.habilidades) == 0:
                self.encerra_sistema()
            for habilidade in lista_habilidades_escolhidas:
                boxeador.habilidades.append(habilidade)

            self.__boxeador_dao.add(boxeador)
            self.__tela_boxeador.mostrar_mensagem('Boxeador cadastrado com sucesso!')
            self.__numero_inscricao += 1

    def gerar_boxeador(self):
        numero_inscricao = 10
        caracteristica_boxeador_facil = Caracteristica(
                forca=10,
                esquiva=10,
                vida=100,
                defesa=10,
                stamina=10,
            )
        caracteristica_boxeador_medio = Caracteristica(
                forca=10,
                esquiva=12,
                vida=125,
                defesa=13,
                stamina=12,
            )
        caracteristica_boxeador_dificil = Caracteristica(
                forca=12,
                esquiva=15,
                vida=150,
                defesa=15,
                stamina=15,
            )
        boxeador_facil = Boxeador(
            nome='Tony Tucker',
            apelido='Tucker',
            idade=30,
            peso=100,
            altura=1.90,
            nacionalidade='EUA',
            cpf=128756789,
            caracteristica=caracteristica_boxeador_facil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao
            )
        self.__boxeador_dao.add(boxeador_facil)
        boxeador_medio = Boxeador(
            nome='John Ruiz',
            apelido='Ruiz',
            idade=33,
            peso=75,
            altura=1.81,
            nacionalidade='EUA',
            cpf=122456129,
            caracteristica=caracteristica_boxeador_medio,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeador_dao.add(boxeador_medio)
        boxeador_dificil = Boxeador(
            nome='Mike Tyson',
            apelido='Tyson',
            idade=30,
            peso=100,
            altura=1.90,
            nacionalidade='EUA',
            cpf=123456555,
            caracteristica=caracteristica_boxeador_dificil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeador_dao.add(boxeador_dificil)
        boxeador_facil_1 = Boxeador(
            nome='Fabiano Pena',
            apelido='Pena',
            idade=24,
            peso=76,
            altura=1.78,
            nacionalidade='BRA',
            cpf=123454321,
            caracteristica=caracteristica_boxeador_facil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeador_dao.add(boxeador_facil_1)
        boxeador_medio_1 = Boxeador(
            nome='Jorge Silva',
            apelido='Silva',
            idade=33,
            peso=75,
            altura=1.81,
            nacionalidade='BRA',
            cpf=123156789,
            caracteristica=caracteristica_boxeador_medio,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeador_dao.add(boxeador_medio_1)
        boxeador_dificil_1 = Boxeador(
            nome='Jean Hauck',
            apelido='GOAT',
            idade=18,
            peso=135,
            altura=2.23,
            nacionalidade='UFSC',
            cpf=121756789,
            caracteristica=caracteristica_boxeador_dificil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeador_dao.add(boxeador_dificil_1)
        boxeador_dificil_2 = Boxeador(
            nome='Anderson Popó',
            apelido='Popó',
            idade=35,
            peso=80,
            altura=1.87,
            nacionalidade='Brasil',
            cpf=123436749,
            caracteristica=caracteristica_boxeador_dificil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeador_dao.add(boxeador_dificil_2)

    def listar_boxeadores(self):
        # Lista os usuarios presentes na lista
        if not self.__boxeador_dao.is_empty():
            boxeadores_usuarios_cadastrados = []
            for boxeador in self.__boxeador_dao.get_all():
                boxeadores_usuarios_cadastrados.append({'nome':boxeador.nome,
                                                      'cpf':boxeador.cpf,
                                                      'apelido': boxeador.apelido,
                                                      'idade': boxeador.idade,
                                                      'peso': boxeador.peso,
                                                      'altura': boxeador.altura,
                                                      'nacionalidade': boxeador.nacionalidade,
                                                      'CPU': boxeador.boxeador_cpu
                                                      })
            self.__tela_boxeador.mostra_boxeador(boxeadores_usuarios_cadastrados)
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador de usuário cadastrado!")

    def listar_boxeadores_edicao_exclusao(self):
        # Lista os usuarios presentes na lista
        if not self.boxeador_dao_usuario_is_empty():
            boxeadores_usuarios_cadastrados = []
            for boxeador in self.__boxeador_dao.get_all():
                if boxeador.boxeador_cpu is False:
                    boxeadores_usuarios_cadastrados.append({'nome':boxeador.nome,
                                                          'cpf':boxeador.cpf,
                                                          'apelido': boxeador.apelido,
                                                          'idade': boxeador.idade,
                                                          'peso': boxeador.peso,
                                                          'altura': boxeador.altura,
                                                          'nacionalidade': boxeador.nacionalidade,
                                                          'CPU': boxeador.boxeador_cpu
                                                          })
            self.__tela_boxeador.mostra_boxeador(boxeadores_usuarios_cadastrados)
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador de usuário cadastrado!")

    def listar_habilidade_boxeador(self):
        if not self.boxeador_dao_usuario_is_empty():
            self.listar_boxeadores_edicao_exclusao()
            cpf = self.__tela_boxeador.obtem_cpf()
            boxeador = self.busca_por_cpf(cpf)
            lista_habilidades_boxeador = []
            if (boxeador is not None):
                for habilidade in boxeador.habilidades:
                    if habilidade.tipo == 'Ataque':
                        lista_habilidades_boxeador.append({'id':habilidade.id,
                                                           'nome':habilidade.nome,
                                                           'dano':habilidade.dano,
                                                           'descricao':habilidade.descricao,
                                                           'custo':habilidade.custo,
                                                           'tipo': 'Ataque'})
                    elif habilidade.tipo == 'Defesa':
                        lista_habilidades_boxeador.append({'id':habilidade.id,
                                                              'nome':habilidade.nome,
                                                              'taxa_defesa':habilidade.taxa_defesa,
                                                              'descricao':habilidade.descricao,
                                                              'custo':habilidade.custo,
                                                                'tipo': 'Defesa'})
                    elif habilidade.tipo == 'Esquiva':
                        lista_habilidades_boxeador.append({'id':habilidade.id,
                                                                'nome':habilidade.nome,
                                                                'taxa_esquiva':habilidade.taxa_esquiva,
                                                                'descricao':habilidade.descricao,
                                                                'custo':habilidade.custo,
                                                                'tipo': 'Esquiva'})
                self.__tela_boxeador.lista_habilidades(lista_habilidades_boxeador)

            else:
                self.__tela_boxeador.mostrar_mensagem("CUIDADO: ESTE BOXEADOR NÃO EXISTE!")
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador de usuário cadastrado!")

    def listar_caracteristica_boxeador(self):
        if not self.boxeador_dao_usuario_is_empty():
            self.listar_boxeadores_edicao_exclusao()
            cpf = self.__tela_boxeador.obtem_cpf()
            boxeador = self.busca_por_cpf(cpf)
            if (boxeador is not None):
                lista_caracteristica_boxeador = []
                lista_caracteristica_boxeador.append({'forca':boxeador.caracteristica.forca,
                                                    'esquiva':boxeador.caracteristica.esquiva,
                                                    'vida':boxeador.caracteristica.vida,
                                                    'defesa':boxeador.caracteristica.defesa,
                                                    'stamina':boxeador.caracteristica.stamina})

                self.__tela_boxeador.mostrar_caracteristica_boxeador(lista_caracteristica_boxeador)
            else:
                self.__tela_boxeador.mostrar_mensagem("CUIDADO: ESTE BOXEADOR NÃO EXISTE!")
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador de usuário cadastrado!")

    def alterar_boxeador(self):
        if not self.boxeador_dao_usuario_is_empty():
            self.listar_boxeadores_edicao_exclusao()
            self.__tela_boxeador.mostrar_mensagem("Insira o CPF do boxeador que deseja alterar")
            cpf = self.__tela_boxeador.obtem_cpf()
            boxeador = self.busca_por_cpf(cpf)
            if (boxeador is not None):
                self.__tela_boxeador.mostrar_mensagem("Insira o CPF do boxeador para alteração")
                novos_dados = self.__tela_boxeador.cadastrar_boxeador()
                boxeador.nome = novos_dados["nome"]
                boxeador.apelido = novos_dados["apelido"]
                boxeador.idade = novos_dados["idade"]
                boxeador.peso = novos_dados["peso"]
                boxeador.altura = novos_dados["altura"]
                boxeador.nacionalidade = novos_dados["nacionalidade"]
                boxeador.boxeador_cpu = False
                self.listar_boxeadores_edicao_exclusao()
                self.__tela_boxeador.mostrar_mensagem("Boxeador alterado com sucesso!")
            else:
                self.__tela_boxeador.mostrar_mensagem("CUIDADO: ESTE BOXEADOR NÃO EXISTE!")
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador editável cadastrado!")

    def excluir_boxeador(self):
        # Exclui boxeador na lista de boxeador
        if not self.boxeador_dao_usuario_is_empty():
            self.listar_boxeadores_edicao_exclusao()
            self.__tela_boxeador.mostrar_mensagem("Insira o CPF do boxeador que deseja excluir")
            cpf_usuario = self.__tela_boxeador.obtem_cpf()
            usuario = self.busca_por_cpf(cpf_usuario)

            if (usuario is not None):
                self.__boxeador_dao.remove(usuario)
                self.listar_boxeadores_edicao_exclusao()
                self.__tela_boxeador.mostrar_mensagem("Boxeador excluído com sucesso!")
            else:
                self.__tela_boxeador.mostrar_mensagem("CUIDADO: ESTE BOXEADOR NÃO EXISTE!")
        else:
            self.__tela_boxeador.mostrar_mensagem("Não há nenhum boxeador editável cadastrado!")

    def cadastrar_caracteristicas(self):
        dict_caracterisitca = self.__tela_caracteristica.tela_cadastro_status()
        return dict_caracterisitca

    def escolher_habilidades(self):
        habilidades = self.__controlador_central.controlador_habilidade.adicionar_habilidade()
        return habilidades

    def listar_caracteristicas(self, boxeador:Boxeador):
        return boxeador.caracteristica

    def verifica_jogadores_maquina(self):
        lista_jogadores_usuario = []
        for boxeador in self.__boxeador_dao.get_all():
            if boxeador.boxeador_cpu is False:
                lista_jogadores_usuario.append(boxeador)
        if len(lista_jogadores_usuario) == 0 or len(lista_jogadores_usuario) > 1:
            self.__tela_boxeador.mostrar_mensagem("---------------------------ATENÇÃO--------------------------------"
                                                  "--")
            self.__tela_boxeador.mostrar_mensagem("Não é possível iniciar o jogo, você tem que controlar 1 jogador!")
            self.__tela_boxeador.mostrar_mensagem("Por favor, cadastre um jogador e marque a opção de que ele não "
                                                  "é CPU")
            self.__tela_boxeador.mostrar_mensagem("------------------------------------------------------------------"
                                                  "--")
            self.encerra_sistema()

    def bonificacao_por_peso(self):
        for boxeador in self.__boxeador_dao.get_all():
            imc = float(boxeador.peso / (boxeador.altura * boxeador.altura))
            if imc < 17:
                boxeador.caracteristica.forca -= 5
                boxeador.caracteristica.esquiva += 7
                boxeador.caracteristica.stamina += 5
            elif 17 <= imc <= 18.49:
                boxeador.caracteristica.forca -= 2
                boxeador.caracteristica.esquiva += 5
                boxeador.caracteristica.stamina += 3
            elif 30 <= imc <= 34.99:
                boxeador.caracteristica.forca += 2
                boxeador.caracteristica.esquiva -= 3
                boxeador.caracteristica.stamina -= 2
            elif imc > 35:
                boxeador.caracteristica.forca += 5
                boxeador.caracteristica.esquiva -= 5
                boxeador.caracteristica.stamina -= 4
    def encerra_sistema(self):
        self.__controlador_central.abre_tela()

    def abre_tela(self):

        escolha_tela = {1: self.cadastrar_boxeador,
                        2: self.alterar_boxeador,
                        3: self.listar_boxeadores,
                        4: self.excluir_boxeador,
                        5: self.listar_habilidade_boxeador,
                        6: self.listar_caracteristica_boxeador,
                        0: self.encerra_sistema}

        continua = True
        while continua:
            escolha_tela[self.__tela_boxeador.primeira_tela_opcoes()]()

    def retornar_boxeadores_cpu(self):
        lista_boxeadores_cpu = []
        for boxeador in self.__boxeador_dao.get_all():
            if boxeador.boxeador_cpu is True:
                lista_boxeadores_cpu.append(boxeador)
        return lista_boxeadores_cpu

    def boxeador_dao_usuario_is_empty(self):
        lista_boxeadores_usuario = []
        for boxeador in self.__boxeador_dao.get_all():
            if boxeador.boxeador_cpu is False:
                lista_boxeadores_usuario.append(boxeador)
        if len(lista_boxeadores_usuario) == 0:
            return True
