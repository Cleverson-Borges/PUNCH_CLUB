class Caracteristica:
    def __init__(self, forca:int, esquiva:int, vida, defesa:int, stamina:int):
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
        if isinstance(vida, float) or isinstance(vida, int):
            self.__vida = vida
        else:
            raise TypeError('A vida deve ser um inteiro ou um float')

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
