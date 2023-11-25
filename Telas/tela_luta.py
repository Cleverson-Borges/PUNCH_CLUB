from Telas.tela_central import TelaAbstrata


class TelaLuta(TelaAbstrata):
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

    def obtem_id(self, lista_inteiro=None):
        if lista_inteiro:
            resposta = self.le_num_inteiro("Escolha qual habilidade que você deseja usar: ",lista_inteiro)
            return resposta
        resposta = self.le_num_inteiro("Escolha qual habilidade que você deseja usar: ", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        return resposta

    def tela_inicio_luta_opcoes(self):
        print()
        print("---------------------------------------------")
        print("| [1] Lutar          |          [0] Desistir|")
        print("---------------------------------------------")
        print()
        opcao = self.le_num_inteiro("Informe sua escolha: ", [0, 1])
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
        print()

    def tela_luta_padrao(self, vida1, vida2, stamina1, stamina2, nacionalidade1, nacionalidade2, apelido1, apelido2):
        lutador1 = [
            f"     {vida1} HP    {stamina1} ST",
            f"",
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
            f"                       {vida2} HP    {stamina2} ST",
            f"",
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
            f"     {vida1} HP    {stamina1} ST",
            f"",
            f"          [{apelido1}]",
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
            f"                       {vida2} HP    {stamina2} ST",
            f"",
            f"                            [{apelido2}]",
            "                           --|||--",
            "                          | _   _ |",
            "                        (  X _ X  )",
            "                          |   ()  |",
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
            f"     {vida1} HP    {stamina1} ST",
            f"",
            f"          {apelido1}",
            "        |||||||||",
            "        | _   _ |",
            "       (  X _ X  )",
            "        |   ()   |",
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
            f"                       {vida2} HP    {stamina2} ST",
            f"",
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

    def mostra_informacoes_luta_usuario(self, dano_total, habilidades_usadas):
        print()
        print('-------------- RELATÓRIO FINAL DA LUTA --------------')
        print()
        print(f"Você causou {dano_total} de dano")
        print(f"Você usou {habilidades_usadas - 1} habilidades")
        print()
        print("-----------------------------------------------------")

    def mostrar_final(self, jogador_usuario, jogador_adversario):
        print()
        print()
        print("               ------ GRANDE FINAL ------               ")
        print()
        print()
        print("----------------------------------------------------------------")
        print(f"|[{jogador_usuario.apelido}] VS [{jogador_adversario.apelido}]|")
        print("----------------------------------------------------------------")

    def mostrar_semi_final(self, jogador_usuario, jogador_adversario):
        print()
        print("               ------ SEMI FINAL ------               ")
        print()
        print("----------------------------------------------------------------")
        print(f"|[{jogador_usuario.apelido}] VS [{jogador_adversario.apelido}]|")
        print("----------------------------------------------------------------")

    def mostrar_campeao(self, jogador):
        print()
        print("               !!!!!! CAMPEÃO !!!!!!               ")
        print()
        print()
        print(f"O {jogador.apelido} ganhou o torneio")
        print(f"Parabéns {jogador.nome}!")
        print()
        print("-----------------------------------------")
        print("-------------- FIM DE JOGO --------------")
        print("-----------------------------------------")
    def mostrar_mensagem(self, mensagem):
        print(mensagem)
