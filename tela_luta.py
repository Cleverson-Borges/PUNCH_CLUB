class TelaLuta:
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

    def obtem_id(self):
        resposta = self.le_num_inteiro("Escolha qual habilidade que você deseja usar", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        return resposta

    def tela_inicio_luta_opcoes(self):
        print("1 Lutar          |          0 Desistir")
        print()
        opcao = self.le_num_inteiro("Escolha a opcao: ", [0, 1])
        return opcao

    def mostrar_habilidade_ataque (self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Dano da habilidade: {habilidade.dano}")
        print()

    def mostrar_habilidade_defesa(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de Defesa: {habilidade.taxa_defesa}")
        print()

    def mostrar_habilidade_esquiva(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de esquiva: {habilidade.taxa_esquiva}")

    def tela_luta_padrao(self, vida1, vida2, stamina1, stamina2, nacionalidade1, nacionalidade2, apelido1, apelido2):
        lutador1 = [
            f" {vida1} HP    {stamina1} ST",
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
            f" {vida2} HP    {stamina2} ST",
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


    def tela_luta_vitoria_boxeador_um(self, vida1, vida2, stamina1, stamina2, nacionalidade1, nacionalidade2, apelido1, apelido2):
        lutador1 = [
            f" {vida1} HP    {stamina1} ST",
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
            f" {vida2} HP    {stamina2} ST",
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


    def tela_luta_vitoria_boxeador_dois(self, vida1, vida2, stamina1, stamina2, nacionalidade1, nacionalidade2, apelido1, apelido2):
        lutador1 = [
            f" {vida1} HP    {stamina1} ST",
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
            f" {vida2} HP    {stamina2} ST",
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

    def mostra_mensagem(self, mensagem):
        print(mensagem)