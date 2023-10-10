from habilidade import Habilidade


class Esquiva(Habilidade):
    def __init__(self, nome, descricao, tipo, custo, taxa_esquiva:int):
        super().__init__(nome, descricao, tipo, custo)
        self.__taxa_esquiva = taxa_esquiva
        Esquiva.adicionar_habilidade(self)


    @property
    def taxa_esquiva(self):
        return self.__taxa_esquiva

    @taxa_esquiva.setter
    def taxa_esquiva(self, taxa_esquiva):
        if isinstance(taxa_esquiva, int):
            self.__taxa_esquiva = taxa_esquiva
        else:
            raise TypeError('A taxa de esquiva deve ser um inteiro')