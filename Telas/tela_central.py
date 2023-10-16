from Telas.tela_abstrata import TelaAbstrata


class TelaCentral(TelaAbstrata):
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
                print("Valor inválido!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def tela_opcoes(self):
        print()
        print(" ----------------------")
        print("   ░▒▓█ PUNCH CLUB █▓▒░")
        print()
        print("1 - CADASTRO DE BOXEADOR")
        print("2 - CADASTRO DE TORNEIO")
        print(" ----------------------")
        print("3 -  ░▓ START GAME ▓░")
        print(" ----------------------")
        print("0 -      SAIR")
        print(" ----------------------")
        print()
        opcao = self.le_num_inteiro("Informe sua escolha: ", [0, 1, 2, 3])
        print()
        return opcao
