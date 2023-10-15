class TelaCentral:
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

    def tela_opcoes(self):
        print("   ░▒▓█ PUNCH CLUB █▓▒░")
        print()
        print("1 Cadastro de boxeador")
        print("2 Cadastro de torneio")
        print(" ---------------------")
        print("3   ░▓ START GAME ▓░")
        print(" ---------------------")
        print("0 -      SAIR")
        print()
        opcao = self.le_num_inteiro("Escolha a opcao: ", [0, 1, 2, 3])
        return opcao
