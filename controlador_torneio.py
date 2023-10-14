from Entidades.torneio import Torneio
from Telas.tela_torneio import TelaTorneio
from Entidades.luta import Luta
from Entidades.boxeador import Boxeador
from Controladores.controlador_boxeador import ControleBoxeador
import random


class ControladorTorneio:
    def __init__(self, nome_torneio: str, numero_lutadores: int):
        self.__nome_torneio = nome_torneio
        self.__numero_lutadores = numero_lutadores
        self.__boxeadores = ControleBoxeador.boxeadores
        self.__tela_torneio = TelaTorneio
        self.__lutas = []

    @property
    def nome_torneio(self):
        return self.__nome_torneio

    @property
    def numero_lutadores(self):
        return self.__numero_lutadores

    @nome_torneio.setter
    def nome_torneio(self, nome):
        self.__nome_torneio = nome

    @numero_lutadores.setter
    def numero_lutadores(self, numero):
        self.__numero_lutadores = numero

    def verifica_entrada_lutadores(self, num):
        while not(num == 4) or (num == 8):
            print("Entrada Inválida")
            num = input(int("Informe novamente o numero de lutadores que dejsa no torneio (4 ou 8): "))
        return num

    def cadastrar_torneio(self):
        pass

    def inscrever_lutador(self):
        pass

    def gerar_chaveamento(self):
        self.__tela_torneio.mostrar_chveamento(self.__nome_torneio, self.__boxeadores)


    def gerar_lutas(self):
        for boxeador in range(self.__numero_lutadores):
            boxeador1, boxeador2 = random.sample(self.__boxeadores, 2)
            return boxeador1, boxeador2
