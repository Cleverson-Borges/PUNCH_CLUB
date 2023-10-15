

class TelaHabilidade:
    def __init__(self):
        pass

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def selecionar_tipo(self):
        print('-'*5, "SELEÇÃO DE HABILIDADES!", "-"*5)
        print("\n(0) Voltar")
        print("(1) Habilidades de ataque")
        print("(2) Habilidades de defesa")
        print("(3) Habilidades de esquiva")
        escolha = self.le_num_inteiro("Escolha a opcao: ", [0, 1, 2, 3])
        return escolha

    def mostrar_habilidade_ataque(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Dano da habilidade: {habilidade.dano}")
        print()

    def mostrar_habilidade_defesa(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de Defesa: {habilidade.taxa_defesa}")
        print()

    def mostrar_habilidade_esquiva(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de esquiva: {habilidade.taxa_esquiva}")
        print()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def obtem_id(self):
        resposta = self.le_num_inteiro("Digite o ID da Habilidade que deseja adicionar ao seu boxeador ou 0 "
                                       "para voltar: ", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        return resposta
