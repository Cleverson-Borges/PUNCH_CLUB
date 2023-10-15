from Controladores.controlador_boxeador import ControladorBoxeador
from Controladores.controlador_habilidade import ControladorHabilidade
from Controladores.controlador_luta import ControladorLuta
from Controladores.controlador_torneio import ControladorTorneio
from Telas.tela_central import TelaCentral


class ControladorCentral:
    def __init__(self):
        self.__controlador_boxeador = ControladorBoxeador(self)
        self.__controlador_habilidade = ControladorHabilidade(self)
        self.__controlador_luta = ControladorLuta(self)
        self.__controlador_torneio = ControladorTorneio(self)
        self.__tela_central = TelaCentral()


    def inicializa_sistema(self):
        self.abre_tela()

    @property
    def controlador_boxeador(self):
        return self.__controlador_boxeador

    @property
    def controlador_habilidade(self):
        return self.__controlador_habilidade

    @property
    def controlador_luta(self):
        return self.__controlador_luta

    @property
    def controlador_torneio(self):
        return self.__controlador_torneio

    def cria_base_dados(self):
        self.__controlador_boxeador.gerar_boxeador()
        self.__controlador_habilidade.gerar_base_de_habilidades()
    def cadastra_boxeador(self):
        self.__controlador_boxeador.abre_tela()
        self.cria_base_dados()

    def cadastra_torneio(self):
        self.__controlador_torneio.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_boxeador,
                        2: self.__controlador_torneio.abre_tela,
                        3: self.__controlador_luta.iniciar_luta}
        while True:
            opcao_escolhida = self.__tela_central.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
