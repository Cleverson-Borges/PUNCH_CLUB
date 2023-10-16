from Entidades.boxeador import Boxeador


class Luta:
    def __init__(self, boxeador_um, boxeador_dois):
        self.__boxeador_um = boxeador_um
        self.__boxeador_dois = boxeador_dois
        self.__vencedor = None
        self.__perdedor = None
        self.__round_atual = 0

    @property
    def boxeador_um(self):
        return self.__boxeador_um

    @property
    def boxeador_dois(self):
        return self.__boxeador_dois

    @property
    def vencedor(self):
        return self.__vencedor

    @property
    def perdedor(self):
        return self.__perdedor

    @property
    def round_atual(self):
        return self.__round_atual

    @boxeador_um.setter
    def boxeador_um(self, lutador_um):
        if isinstance(lutador_um, Boxeador):
            self.__boxeador_um = lutador_um
        else:
            raise TypeError('O lutador deve ser um boxeador')

    @boxeador_dois.setter
    def boxeador_dois(self, lutador_dois):
        if isinstance(lutador_dois, Boxeador):
            self.__boxeador_dois = lutador_dois
        else:
            raise TypeError('O lutador deve ser um boxeador')

    @vencedor.setter
    def vencedor(self, vencedor):
        if isinstance(vencedor, Boxeador):
            self.__vencedor = vencedor
        else:
            raise TypeError('O lutador deve ser um boxeador')

    @perdedor.setter
    def perdedor(self, perdedor):
        if isinstance(perdedor, Boxeador):
            self.__perdedor = perdedor
        else:
            raise TypeError('O lutador deve ser um boxeador')

    @round_atual.setter
    def round_atual(self, round_atual):
        if isinstance(round_atual, int):
            self.__round_atual = round_atual
        else:
            raise TypeError('O round deve ser um inteiro')
