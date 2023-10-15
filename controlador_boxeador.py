from Entidades.boxeador import Boxeador
from Entidades.caracteristica import Caracteristica
from Telas.tela_caracteristica import TelaCaracteristica
from Telas.tela_boxeador import TelaBoxeador


class ControladorBoxeador:
    def __init__(self, controlador_central):
        self.__tela_boxeador = TelaBoxeador()
        self.__tela_caracteristica = TelaCaracteristica()
        self.__controlador_central = controlador_central
        self.__boxeadores = []
        self.__boxeador_atual = None
        self.__numero_inscricao = 1

    @property
    def boxeadores(self):
        return self.__boxeadores

    @property
    def boxeador_atual(self):
        return self.__boxeador_atual

    @boxeador_atual.setter
    def boxeador_atual(self, boxeador:Boxeador):
        if isinstance(boxeador, Boxeador):
            self.__boxeador_atual = boxeador
        else:
            raise TypeError('O boxeador deve ser uma instância da classe Boxeador')

    def busca_por_cpf(self, cpf):
        # Busca um usuário na lista de boxeadors com base no CPF
        for boxeador in self.__boxeadores:
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
            # dicionario_informacoes_boxeador = self.__tela_boxeador.cadastrar_boxeador()
            # dicionario_informacoes_boxeador['cpf'] = cpf
            # dicionario_informacoes_caracteristica = self.cadastrar_caracteristicas()
            # boxeador_cpu = self.__tela_boxeador.verifica_boxeador_cpu()
            # if boxeador_cpu == 'S' or boxeador_cpu == 'Sim' or boxeador_cpu == 'sim':
            #     boxeador_cpu = True
            # else:
            #     boxeador_cpu = False
            # caracteristicas_boxeador = Caracteristica(
            #     forca=dicionario_informacoes_caracteristica['forca'],
            #     esquiva=dicionario_informacoes_caracteristica['esquiva'],
            #     vida=dicionario_informacoes_caracteristica['vida'],
            #     defesa=dicionario_informacoes_caracteristica['defesa'],
            #     stamina=dicionario_informacoes_caracteristica['stamina'],
            # )
            #
            # boxeador = Boxeador(
            #     nome=dicionario_informacoes_boxeador['nome'],
            #     apelido=dicionario_informacoes_boxeador['apelido'],
            #     idade=dicionario_informacoes_boxeador['idade'],
            #     peso=dicionario_informacoes_boxeador['peso'],
            #     altura=dicionario_informacoes_boxeador['altura'],
            #     nacionalidade=dicionario_informacoes_boxeador['nacionalidade'],
            #     cpf=dicionario_informacoes_boxeador['cpf'],
            #     caracteristica=caracteristicas_boxeador,
            #     boxeador_cpu=boxeador_cpu,
            #     numero_inscricao=self.__numero_inscricao
            # )
            exemplo_caracteristica = Caracteristica(
                    forca=10,
                    esquiva=10,
                    vida=10,
                    defesa=10,
                    stamina=10,
                )
            boxeador = Boxeador(
                nome='ds',
                apelido='ds',
                idade=12,
                peso=43,
                altura=543,
                nacionalidade='ds',
                cpf=cpf,
                caracteristica=exemplo_caracteristica,
                numero_inscricao=self.__numero_inscricao,
                boxeador_cpu=True
            )
            # lista_habilidades_escolhidas = self.escolher_habilidades()
            # if lista_habilidades_escolhidas is None and len(boxeador.habilidades) == 0:
            #     self.encerra_sistema()
            # for habilidade in lista_habilidades_escolhidas:
            #     boxeador.habilidades.append(habilidade)

            self.__boxeadores.append(boxeador)
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
                vida=150,
                defesa=13,
                stamina=10,
            )
        caracteristica_boxeador_dificil = Caracteristica(
                forca=12,
                esquiva=15,
                vida=200,
                defesa=15,
                stamina=10,
            )
        boxeador_facil = Boxeador(
            nome='Tony Tucker',
            apelido='Tucker',
            idade=30,
            peso=100,
            altura=1.90,
            nacionalidade='Estados Unidos',
            cpf=128756789,
            caracteristica=caracteristica_boxeador_facil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao
            )
        self.__boxeadores.append(boxeador_facil)
        boxeador_medio = Boxeador(
            nome='John Ruiz',
            apelido='Ruiz',
            idade=33,
            peso=75,
            altura=1.81,
            nacionalidade='Estados Unidos',
            cpf=122456129,
            caracteristica=caracteristica_boxeador_medio,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeadores.append(boxeador_medio)
        boxeador_dificil = Boxeador(
            nome='Mike Tyson',
            apelido='Tyson',
            idade=30,
            peso=100,
            altura=1.90,
            nacionalidade='Estados Unidos',
            cpf=123456555,
            caracteristica=caracteristica_boxeador_dificil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeadores.append(boxeador_dificil)
        boxeador_facil_1 = Boxeador(
            nome='Fabiano Pena',
            apelido='Pena',
            idade=24,
            peso=76,
            altura=1.78,
            nacionalidade='Brasil',
            cpf=123454321,
            caracteristica=caracteristica_boxeador_facil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeadores.append(boxeador_facil_1)
        boxeador_medio_1 = Boxeador(
            nome='Jorge Silva',
            apelido='Silva',
            idade=33,
            peso=75,
            altura=1.81,
            nacionalidade='Brasil',
            cpf=123156789,
            caracteristica=caracteristica_boxeador_medio,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeadores.append(boxeador_medio_1)
        boxeador_dificil_1 = Boxeador(
            nome='Rafael Santos',
            apelido='Santos',
            idade=30,
            peso=100,
            altura=1.90,
            nacionalidade='Brasil',
            cpf=121756789,
            caracteristica=caracteristica_boxeador_dificil,
            boxeador_cpu=True,
            numero_inscricao=numero_inscricao + 1
            )
        self.__boxeadores.append(boxeador_dificil_1)
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
        self.__boxeadores.append(boxeador_dificil_2)

    def listar_boxeadores(self):
        # Lista os usuarios presentes na lista
        if len(self.__boxeadores) > 0:
            self.__tela_boxeador.mostrar_mensagem("-----------LISTA DE BOXEADORES-----------")
            for boxeador in self.__boxeadores:
                self.__tela_boxeador.mostra_boxeador({'nome':boxeador.nome,
                                                      'cpf':boxeador.cpf,
                                                      'apelido': boxeador.apelido,
                                                      'idade': boxeador.idade,
                                                      'peso': boxeador.peso,
                                                      'altura': boxeador.altura,
                                                      'nacionalidade': boxeador.nacionalidade,
                                                      'CPU': boxeador.boxeador_cpu
                                                      })
        else:
            self.__tela_boxeador.mostrar_mensagem("A lista está vazia")

    def alterar_boxeador(self):
        if len(self.__boxeadores) > 0:
            self.listar_boxeadores()
            self.__tela_boxeador.mostrar_mensagem("Insira o CPF do boxeador que deseja alterar")
            cpf = self.__tela_boxeador.obtem_cpf()
            boxeador = self.busca_por_cpf(cpf)
            boxeador_cpu = self.__tela_boxeador.verifica_boxeador_cpu()
            if boxeador_cpu == 'S' or boxeador_cpu == 'Sim' or boxeador_cpu == 'sim':
                boxeador_cpu = True
            else:
                boxeador_cpu = False
            if (boxeador is not None):
                self.__tela_boxeador.mostrar_mensagem("Insira o CPF do boxeador para alteração")
                novos_dados = self.__tela_boxeador.cadastrar_boxeador()
                boxeador.nome = novos_dados["nome"]
                boxeador.apelido = novos_dados["apelido"]
                boxeador.idade = novos_dados["idade"]
                boxeador.peso = novos_dados["peso"]
                boxeador.altura = novos_dados["altura"]
                boxeador.nacionalidade = novos_dados["nacionalidade"]
                boxeador.boxeador_cpu = boxeador_cpu
                self.listar_boxeadores()
                self.__tela_boxeador.mostrar_mensagem("Boxeador alterado com sucesso")
            else:
                self.__tela_boxeador.mostrar_mensagem("CUIDADO: ESTE ATIVO NÃO EXISTE")
        else:
            self.__tela_boxeador.mostrar_mensagem("A lista está vazia")

    def excluir_boxeador(self):
        # Exclui boxeador na lista de boxeador
        if len(self.__boxeadores) > 0:
            self.listar_boxeadores()
            self.__tela_boxeador.mostrar_mensagem("Insira o CPF do boxeador que deseja excluir")
            cpf_usuario = self.__tela_boxeador.obtem_cpf()
            usuario = self.busca_por_cpf(cpf_usuario)

            if (usuario is not None):
                self.__boxeadores.remove(usuario)
                self.listar_boxeadores()
                self.__tela_boxeador.mostrar_mensagem("Boxeador excluído com sucesso")
            else:
                self.__tela_boxeador.mostrar_mensagem("CUIDADO: ESTE USUÁRIO NÃO EXISTE")
        else:
            self.__tela_boxeador.mostrar_mensagem("A lista está vazia")

    def cadastrar_caracteristicas(self):
        dict_caracterisitca = self.__tela_caracteristica.tela_cadastro_status()
        return dict_caracterisitca

    def escolher_habilidades(self):
        self.__controlador_central.controlador_habilidade.gerar_base_de_habilidades()
        habilidades = self.__controlador_central.controlador_habilidade.adicionar_habilidade()
        return habilidades

    def listar_habilidades(self, boxeador:Boxeador):
        return boxeador.habilidades


    def verifica_jogadores_maquina(self):
        lista_jogadores_usuario = []
        for boxeador in self.__boxeadores:
            if boxeador.boxeador_cpu is False:
                lista_jogadores_usuario.append(boxeador)
        if len(lista_jogadores_usuario) == 0 or len(lista_jogadores_usuario) > 1:
            self.__tela_boxeador.mostrar_mensagem("---------------------------ATENÇÃO---------------------------")
            self.__tela_boxeador.mostrar_mensagem("Não é possível iniciar o jogo, você tem que controlar 1 jogador!")
            self.__tela_boxeador.mostrar_mensagem("Por favor, cadastre um jogador e marque a opção de que ele não é CPU")
            self.__tela_boxeador.mostrar_mensagem("------------------------------------------------------------")
            self.encerra_sistema()
    def encerra_sistema(self):
        self.__controlador_central.abre_tela()

    def abre_tela(self):

        escolha_tela = {1: self.cadastrar_boxeador,
                        2: self.alterar_boxeador,
                        3: self.listar_boxeadores,
                        4: self.excluir_boxeador,
                        0: self.encerra_sistema}

        continua = True
        while continua:
            escolha_tela[self.__tela_boxeador.tela_opcoes()]()
