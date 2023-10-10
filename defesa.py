from habilidade import Habilidade


class Defesa(Habilidade):
    def __init__(self, nome, descricao, tipo, custo, taxa_defesa:int):
        super().__init__(nome, descricao, tipo, custo)
        self.__taxa_defesa = taxa_defesa
        Defesa.adicionar_habilidade(self)

    @property
    def taxa_defesa(self):
        return self.__taxa_defesa

    @taxa_defesa.setter
    def taxa_defesa(self, taxa_defesa):
        if isinstance(taxa_defesa, int):
            self.__taxa_defesa = taxa_defesa
        else:
            raise TypeError('A taxa de defesa deve ser um inteiro')