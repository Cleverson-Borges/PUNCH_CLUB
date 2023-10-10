from Entidades.habilidade import Habilidade


class HabilityController:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__habilidades = []
        self.__habilidade_atual = None

    @property
    def habilidades(self):
        return self.__habilidades

    @property
    def habilidade_atual(self):
        return self.__habilidade_atual

    def cadastrar_habilidade(self, habilidade:Habilidade):
        if isinstance(habilidade, Habilidade):
            self.__habilidades.append(habilidade)
        else:
            raise TypeError('A habilidade deve ser uma instância da classe Habilidade')

    def habilidade_atual(self, habilidade):
        if isinstance(habilidade, Habilidade):
            self.__habilidade_atual = habilidade
        else:
            raise TypeError('A habilidade deve ser uma instância da classe Habilidade')
