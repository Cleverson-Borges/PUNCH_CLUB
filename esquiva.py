from Entidades.habilidade import Habilidade


class Esquiva(Habilidade):
    def __init__(self, id, nome, descricao, tipo, custo, taxa_esquiva:int):
        super().__init__(id, nome, descricao, tipo, custo)
        self.__taxa_esquiva = taxa_esquiva

    @property
    def taxa_esquiva(self):
        return self.__taxa_esquiva

    @taxa_esquiva.setter
    def taxa_esquiva(self, taxa_esquiva):
        if isinstance(taxa_esquiva, int):
            self.__taxa_esquiva = taxa_esquiva
        else:
            raise TypeError('A taxa de esquiva deve ser um inteiro')