

class TelaHabilidade():
    def __init__(self):
        pass

    def selecionar_tipo(self):
        print('-'*5,"SELEÇÃO DE HABILIDADES!", "-"*5)
        print("\n(1) Habilidades de ataque")
        print("(2) Habilidades de defesa")
        print("(3) Habilidades de esquiva")
        escolha = input(str("\nQual tipo de habilidade deseja cadastrar: "))
        return escolha

    def mostrar_habilidade(self, habilidade):
        print()
        print(f"Nome : {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo: {habilidade.custo}")
        print()


    def obtem_id(self):
        resposta = input(int("Digite o ID da Habilidade que deseja adicionar ao seu boxeador ou 0 para voltar: "))
        return resposta


