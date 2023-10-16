from Entidades.caracteristica import Caracteristica


class Boxeador:
    def __init__(self, nome:str, apelido:str, idade:int, peso:float, altura:float, nacionalidade:str, cpf:int, caracteristica:Caracteristica, numero_inscricao:int, boxeador_cpu:bool):
        self.__nome = nome
        self.__apelido = apelido
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__nacionalidade = nacionalidade
        self.__cpf = cpf
        self.__caracteristica = caracteristica
        self.__numero_inscricao = numero_inscricao
        self.__boxeador_cpu = boxeador_cpu
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
    def cpf(self):
        return self.__cpf

    @property
    def caracteristica(self):
        return self.__caracteristica

    @property
    def numero_inscricao(self):
        return self.__numero_inscricao

    @property
    def boxeador_cpu(self):
        return self.__boxeador_cpu

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

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf
        else:
            raise TypeError('O CPF deve ser um inteiro')

    @caracteristica.setter
    def caracteristica(self, status):
        if isinstance(status, Caracteristica):
            self.__status = status
        else:
            raise TypeError('O status deve ser um objeto da classe Status')

    @numero_inscricao.setter
    def numero_inscricao(self, numero_inscricao):
        if isinstance(numero_inscricao, int):
            self.__numero_inscricao = numero_inscricao
        else:
            raise TypeError('O número de inscrição deve ser um inteiro')

    @boxeador_cpu.setter
    def boxeador_cpu(self, boxeador_cpu):
        if isinstance(boxeador_cpu, bool):
            self.__boxeador_cpu = boxeador_cpu
        else:
            raise TypeError('Boxeador CPU é False ou True')
