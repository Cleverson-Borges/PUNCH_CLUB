from Entidades.luta import Luta
from Controladores.controlador_luta import ControladorLuta


class Torneio():
    def __init__(self, nome_torneio, numero_lutas):
        self.__nome_torneio = nome_torneio
        self.__numero_lutas = numero_lutas

    @property
    def nome_torneio(self):
        return self.__nome_torneio

    @property
    def numero_lutas(self):
        return self.__numero_lutas

    @nome_torneio.setter
    def nome_torneio(self, nome):
        self.__nome_torneio = nome

    @numero_lutas.setter
    def numero_lutas(self, numero):
        self.__numero_lutas = numero


