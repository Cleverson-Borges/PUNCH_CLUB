from equipamento import Equipamento
from status import Status
from habilidade import Habilidade


class Boxeador:
    def __init__(self, nome:str, apelido:str, idade:int, peso:float, altura:float, nacionalidade:str, equipamento:Equipamento, status:Status):
        self.__nome = nome
        self.__apelido = apelido
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__nacionalidade = nacionalidade
        self.__equipamento = equipamento
        self.__status = status
        self.__numero_inscricao = 1
        self.__habilidades = []
        
    @property
    def nome(self):
        return self.__nome

    @property
    def apelido(self):
        return self.__apelido

    @property
    def idade(self):
        return self.__idade

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def equipamento(self):
        return self.__equipamento

    @property
    def status(self):
        return self.__status

    @property
    def numero_inscricao(self):
        return self.__numero_inscricao

    @property
    def habilidades(self):
        return self.__habilidades

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError('O nome deve ser uma string')


    @apelido.setter
    def apelido(self, apelido):
        if isinstance(apelido, str):
            self.__apelido = apelido
        else:
            raise TypeError('O apelido deve ser uma string')

    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int):
            self.__idade = idade
        else:
            raise TypeError('A idade deve ser um inteiro')

    @peso.setter
    def peso(self, peso):
        if isinstance(peso, float):
            self.__peso = peso
        else:
            raise TypeError('O peso deve ser um float')

    @altura.setter
    def altura(self, altura):
        if isinstance(altura, float):
            self.__altura = altura
        else:
            raise TypeError('A altura deve ser um float')

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        if isinstance(nacionalidade, str):
            self.__nacionalidade = nacionalidade
        else:
            raise TypeError('A nacionalidade deve ser uma string')

    @equipamento.setter
    def equipamento(self, equipamento):
        if isinstance(equipamento, Equipamento):
            self.__equipamento = equipamento
        else:
            raise TypeError('O equipamento deve ser um objeto da classe Equipamento')

    @status.setter
    def status(self, status):
        if isinstance(status, Status):
            self.__status = status
        else:
            raise TypeError('O status deve ser um objeto da classe Status')

    @numero_inscricao.setter
    def numero_inscricao(self, numero_inscricao):
        if isinstance(numero_inscricao, int):
            self.__numero_inscricao = numero_inscricao
        else:
            raise TypeError('O número de inscrição deve ser um inteiro')