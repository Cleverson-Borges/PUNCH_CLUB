from Entidades.habilidade import Habilidade


class Ataque(Habilidade):
    def __init__(self, id, nome, descricao, tipo, custo, dano):
        super().__init__(id, nome, descricao, tipo, custo)
        self.__dano = dano

    @property
    def dano(self):
        return self.__dano

    @dano.setter
    def dano(self, dano):
        if isinstance(dano, int):
            self.__dano = dano
        else:
            raise TypeError('O dano deve ser um inteiro')
