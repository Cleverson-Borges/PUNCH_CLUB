

class TelaHabilidade:
    def __init__(self):
        pass

    def selecionar_tipo(self):
        print('-'*5, "SELEÇÃO DE HABILIDADES!", "-"*5)
        print("\n(1) Habilidades de ataque")
        print("(2) Habilidades de defesa")
        print("(3) Habilidades de esquiva")
        escolha = input(str("\nQual tipo de habilidade deseja cadastrar: "))
        return escolha

    def mostrar_habilidade_ataque(self, habilidade):
        print()
        print("-"*5, "INFORMAÇÕES DAS HABILIDADES DE ATAQUE", "-"*5)
        print()
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Dano da habilidade: {habilidade.dano}")
        print()

    def mostrar_habilidade_defesa(self, habilidade):
        print()
        print("-"*5, "INFORMAÇÕES DAS HABILIDADES DE DEFESA", "-"*5)
        print()
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de Defesa: {habilidade.taxa_defesa}")
        print()

    def mostrar_habilidade_esquiva(self, habilidade):
        print()
        print("-"*5, "INFORMAÇÕES DAS HABILIDADES DE ESQUIVA", "-"*5)
        print()
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de esquiva: {habilidade.taxa_esquiva}")
        print()

    def obtem_id(self):
        resposta = input(int("Digite o ID da Habilidade que deseja adicionar ao seu boxeador ou 0 para voltar: "))
        return resposta
