from Entidades.habilidade import Habilidade


class Defesa(Habilidade):
    def __init__(self, id, nome, descricao, tipo, custo, taxa_defesa:int):
        super().__init__(id, nome, descricao, tipo, custo)
        self.__taxa_defesa = taxa_defesa

    @property
    def taxa_defesa(self):
        return self.__taxa_defesa

    @taxa_defesa.setter
    def taxa_defesa(self, taxa_defesa):
        if isinstance(taxa_defesa, int):
            self.__taxa_defesa = taxa_defesa
        else:
            raise TypeError('A taxa de defesa deve ser um inteiro')