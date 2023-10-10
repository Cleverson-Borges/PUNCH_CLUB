from Entidades.habilidade import Habilidade


class Status:
    def __init__(self, forca:int, esquiva:int, vida:int, defesa:int, stamina:int):
        self.__forca = forca
        self.__esquiva = esquiva
        self.__vida = vida
        self.__defesa = defesa
        self.__stamina = stamina
        self.__xp = 0

    @property
    def forca(self):
        return self.__forca

    @property
    def esquiva(self):
        return self.__esquiva

    @property
    def vida(self):
        return self.__vida

    @property
    def defesa(self):
        return self.__defesa

    @property
    def stamina(self):
        return self.__stamina

    @property
    def xp(self):
        return self.__xp

    @property
    def habilidade(self):
        return self.__habilidade

    @forca.setter
    def forca(self, forca):
        if isinstance(forca, int):
            self.__forca = forca
        else:
            raise TypeError('A força deve ser um inteiro')

    @esquiva.setter
    def esquiva(self, esquiva):
        if isinstance(esquiva, int):
            self.__esquiva = esquiva
        else:
            raise TypeError('A esquiva deve ser um inteiro')

    @vida.setter
    def vida(self, vida):
        if isinstance(vida, int):
            self.__vida = vida
        else:
            raise TypeError('A vida deve ser um inteiro')

    @defesa.setter
    def defesa(self, defesa):
        if isinstance(defesa, int):
            self.__defesa = defesa
        else:
            raise TypeError('A defesa deve ser um inteiro')

    @stamina.setter
    def stamina(self, stamina):
        if isinstance(stamina, int):
            self.__stamina = stamina
        else:
            raise TypeError('A stamina deve ser um inteiro')

    @xp.setter
    def xp(self, xp):
        if isinstance(xp, int):
            self.__xp = xp
        else:
            raise TypeError('O xp deve ser um inteiro')

    @habilidade.setter
    def habilidade(self, habilidade):
        if isinstance(habilidade, Habilidade):
            self.__habilidade = habilidade
        else:
            raise TypeError('A habilidade deve ser uma instância de Habilidade')