from Telas.tela_torneio import TelaTorneio
from Entidades.luta import Luta
from Entidades.torneio import Torneio
import random


class ControladorTorneio:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__tela_torneio = TelaTorneio()
        self.__torneio_atual = None
        self.__lutas = []
        self.__torneio_criado = False

    @property
    def lutas_torneio(self):
        return self.__lutas

    def cadastrar_torneio(self):
        if self.__torneio_criado:
            self.__tela_torneio.mostra_mensagem("Torneio já cadastrado, se quiser altere-o!")
        else:
            informacoes_torneio = self.__tela_torneio.cadastro_torneio()
            nome_torneio = informacoes_torneio["nome_torneio"]
            numero_lutadores = informacoes_torneio["numero_lutadores"]
            self.__torneio_atual = Torneio(nome_torneio, numero_lutadores)
            self.criar_lutas()
            self.__torneio_criado = True

    def alterar_torneio(self):
        if self.__torneio_atual:
            informacoes_torneio = self.__tela_torneio.cadastro_torneio()
            nome_torneio = informacoes_torneio["nome_torneio"]
            numero_lutadores = informacoes_torneio["numero_lutadores"]
            self.__torneio_atual.nome_torneio = nome_torneio
            self.__torneio_atual.numero_lutadores = numero_lutadores
        else:
            self.__tela_torneio.mostra_mensagem("Não há nenhum torneio cadastrado para editar")
    def mostrar_torneio(self):
        if self.__torneio_atual:
            self.__tela_torneio.mostrar_torneio(self.__torneio_atual.nome_torneio, self.__torneio_atual.numero_lutadores)
            for luta in self.__lutas:
                self.__tela_torneio.mostrar_chaveamento(luta.boxeador_um, luta.lutador_dois)
        else:
            self.__tela_torneio.mostra_mensagem("Torneio não cadastrado, é necessário cadastrar o torneio antes")
    def criar_lutas(self):
        lista_boxeadores = self.__controlador_central.controlador_boxeador.boxeadores
        for i in range(len(lista_boxeadores) - 1):
            lutador_um = lista_boxeadores[i]
            lutador_dois = lista_boxeadores[i + 1]
            self.__lutas.append(Luta(lutador_um, lutador_dois))

    def mostrar_luta_usuario(self):
        self.__tela_torneio.mostrar_luta_usuario()

    def gerar_lutas(self):
        lista_boxeadores = self.__controlador_central.controlador_boxeador.boxeadores
        for boxeador in range(lista_boxeadores):
            boxeador1, boxeador2 = random.sample(lista_boxeadores, 2)
            return boxeador1, boxeador2

    def mostrar_chaveamento(self):
        for luta in self.__lutas:
            self.__tela_torneio.mostrar_chaveamento(self.__torneio_atual.nome_torneio, luta.boxeador_um, luta.boxeador_dois, luta.fase)

    def encerra_sistema(self):
        self.__controlador_central.abre_tela()

    def abre_tela(self):

        escolha_tela = {1: self.cadastrar_torneio,
                        2: self.alterar_torneio,
                        3: self.mostrar_torneio,
                        0: self.encerra_sistema}

        continua = True
        while continua:
            escolha_tela[self.__tela_torneio.tela_opcoes()]()
