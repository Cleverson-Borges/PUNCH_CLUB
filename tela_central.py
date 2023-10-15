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


    def tela_luta_padrao(self, nacionalidade1, nacionalidade2, apelido1, apelido2):
        lutador1 = [
            f"          {apelido1}",
            "        |||||||||",
            "        | _   _ |",
            "       (  O _ O  )",
            "        |   _   |",
            "         |_____|",
            "  _______/     \\_______",
            " /                     \\",
            "|   |\\             /|   |",
            "|   ||  .       .  ||   |",
            "|   / \\           / \\   |",
            "\\  |   | |_ | _| |   |  /",
            "|==|   | |_ | _| |   |==|",
            "/  /_ _|_|__|__|_|_ _\\  \\",
            "|___| /            \\|___|",
            "      |     |      |",
            "      |     |      |",
            f"      |{nacionalidade1}  |   {nacionalidade1}|",
            "      |     |      |",
            "      \"|\"|\"\"|\"|\"\"|",
        ]

        lutador2 = [
            f"                            {apelido2}",
            "                           --|||--",
            "                          | _   _ |",
            "                        (  o _ o  )",
            "                          |  ___  |",
            "                            |_____|",
            "              _______/     \\_______",
            "            /                      \\",
            "           |   |\\             /|   |",
            "           |   || \*/     \*/ ||   |",
            "           |   / \\           / \\   |",
            "           \\  |   | |_ | _| |   |  /",
            "           |==|   | |_ | _| |   |==|",
            "           /  /_ _|_|__|__|_|_ _\\  \\",
            "           |___| /            \\|___|",
            "                      |     |      |",
            "                      |     |      |",
            f"                      |{nacionalidade2}  |   {nacionalidade2}|",
            "                      |     |      |",

        ]

        for linha1, linha2 in zip(lutador1, lutador2):
            print(linha1 + "           " + linha2)

    def tela_luta_vitoria_boxeador_um(self, nacionalidade1, nacionalidade2, apelido1, apelido2):
        lutador1 = [
            f"          {apelido1}",
            "        |||||||||",
            "        | _   _ |",
            "       (  O _ O  )",
            "        |   _   |",
            "         |_____|",
            "  _______/     \\_______",
            " /                     \\",
            "|   |\\             /|   |",
            "|   ||  .       .  ||   |",
            "|   / \\           / \\   |",
            "\\  |   | |_ | _| |   |  /",
            "|==|   | |_ | _| |   |==|",
            "/  /_ _|_|__|__|_|_ _\\  \\",
            "|___| /            \\|___|",
            "      |     |      |",
            "      |     |      |",
            f"      |{nacionalidade1}  |   {nacionalidade1}|",
            "      |     |      |",
            "      \"|\"|\"\"|\"|\"\"|",
        ]

        lutador2 = [
            f"                            {apelido2}",
            "                           --|||--",
            "                          | _   _ |",
            "                        (  X _ X  )",
            "                          |   O  |",
            "                            |_____|",
            "              _______/     \\_______",
            "            /                      \\",
            "           |   |\\             /|   |",
            "           |   || \*/     \*/ ||   |",
            "           |   / \\           / \\   |",
            "           \\  |   | |_ | _| |   |  /",
            "           |==|   | |_ | _| |   |==|",
            "           /  /_ _|_|__|__|_|_ _\\  \\",
            "           |___| /            \\|___|",
            "                      |     |      |",
            "                      |     |      |",
            f"                      |{nacionalidade2}  |   {nacionalidade2}|",
            "                      |     |      |",

        ]

        for linha1, linha2 in zip(lutador1, lutador2):
            print(linha1 + "           " + linha2)

    def tela_luta_vitoria_boxeador_dois(self, nacionalidade1, nacionalidade2, apelido1, apelido2):
        lutador1 = [
            f"          {apelido1}",
            "        |||||||||",
            "        | _   _ |",
            "       (  X _ X  )",
            "        |   O   |",
            "         |_____|",
            "  _______/     \\_______",
            " /                     \\",
            "|   |\\             /|   |",
            "|   ||  .       .  ||   |",
            "|   / \\           / \\   |",
            "\\  |   | |_ | _| |   |  /",
            "|==|   | |_ | _| |   |==|",
            "/  /_ _|_|__|__|_|_ _\\  \\",
            "|___| /            \\|___|",
            "      |     |      |",
            "      |     |      |",
            f"      |{nacionalidade1}  |   {nacionalidade1}|",
            "      |     |      |",
            "      \"|\"|\"\"|\"|\"\"|",
        ]

        lutador2 = [
            f"                            {apelido2}",
            "                           --|||--",
            "                          | _   _ |",
            "                        (  o _ o  )",
            "                          |  ___  |",
            "                            |_____|",
            "              _______/     \\_______",
            "            /                      \\",
            "           |   |\\             /|   |",
            "           |   || \*/     \*/ ||   |",
            "           |   / \\           / \\   |",
            "           \\  |   | |_ | _| |   |  /",
            "           |==|   | |_ | _| |   |==|",
            "           /  /_ _|_|__|__|_|_ _\\  \\",
            "           |___| /            \\|___|",
            "                      |     |      |",
            "                      |     |      |",
            f"                      |{nacionalidade2}  |   {nacionalidade2}|",
            "                      |     |      |",

        ]

        for linha1, linha2 in zip(lutador1, lutador2):
            print(linha1 + "           " + linha2)
