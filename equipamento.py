class Equipamento():

    def __init__(self, nome:str, cor:str, tipo_de_buff:str, quantidade_buff:int, peso:float):
        self.__nome = nome
        self.__cor = cor
        self.__tipo_de_buff = tipo_de_buff
        self.__quantidade_buff = quantidade_buff
        self.__peso = peso
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cor(self):
        return self.__cor

    @property
    def tipo_de_buff(self):
        return self.__tipo_de_buff

    @property
    def quantidade_buff(self):
        return self.__quantidade_buff

    @property
    def peso(self):
        return self.__peso
        
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError('O nome deve ser uma string')

    @cor.setter
    def cor(self, cor):
        if isinstance(cor, str):
            self.__cor = cor
        else:
            raise TypeError('A cor deve ser uma string')

    @tipo_de_buff.setter
    def tipo_de_buff(self, tipo_de_buff):
        if isinstance(tipo_de_buff, str):
            self.__tipo_de_buff = tipo_de_buff
        else:
            raise TypeError('O tipo de buff deve ser uma string')

    @quantidade_buff.setter
    def quantidade_buff(self, quantidade_buff):
        if isinstance(quantidade_buff, int):
            self.__quantidade_buff = quantidade_buff
        else:
            raise TypeError('A quantidade de buff deve ser um inteiro')

    @peso.setter
    def peso(self, peso):
        if isinstance(peso, float):
            self.__peso = peso
        else:
            raise TypeError('O peso deve ser um float')