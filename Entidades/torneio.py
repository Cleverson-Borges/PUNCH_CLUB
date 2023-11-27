from Entidades.boxeador import Boxeador
from random import randint
from Entidades.luta import Luta


class Torneio():
    def __init__(self, nome_torneio, id_torneio, lista_lutas=None):
        self.__nome_torneio = nome_torneio
        self.__id_torneio = id_torneio
        self.__boxeador_usuario = None
        self.__lista_lutas = lista_lutas if lista_lutas is not None else []

    @property
    def nome_torneio(self):
        return self.__nome_torneio


    @property
    def id_torneio(self):
        return self.__id_torneio

    @property
    def boxeador_usuario(self):
        return self.__boxeador_usuario

    @property
    def lista_lutas(self):
        return self.__lista_lutas

    @nome_torneio.setter
    def nome_torneio(self, nome):
        if isinstance(nome, str):
            self.__nome_torneio = nome

    @id_torneio.setter
    def id_torneio(self, id):
        if isinstance(id, int):
            self.__id_torneio = id

    @boxeador_usuario.setter
    def boxeador_usuario(self, boxeador):
        if isinstance(boxeador, Boxeador):
            self.__boxeador_usuario = boxeador

    @lista_lutas.setter
    def lista_lutas(self, lista_lutas):
        if isinstance(lista_lutas, list):
            self.lista_lutas = lista_lutas

    def adicionar_luta(self, luta):
        if isinstance(luta, Luta):
            self.__lista_lutas.append(luta)
