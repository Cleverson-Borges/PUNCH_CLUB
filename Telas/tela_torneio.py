from Telas.tela_central import TelaAbstrata


class TelaTorneio(TelaAbstrata):
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

    def cadastro_torneio(self):
        print("-"*15, "CADASTRAMENTO DE TORNEIO", "-"*15)
        print()
        nome_torneio = input(str("Informe o nome que deseja dar ao torneio PUNCH CLUB: "))
        numero_lutadores = self.le_num_inteiro("Informe novamente o numero de lutadores que deseja no "
                                               "torneio (4 ou 8): ", [4, 8])
        return {"nome_torneio": nome_torneio,
                "numero_lutadores": numero_lutadores}

    def alterar_torneio(self):
        print("-"*15, "ALTERAR NOME DO TORNEIO", "-"*15)
        print()
        nome_torneio = input(str("Informe o novo nome que deseja dar ao torneio PUNCH CLUB: "))
        print()
        return {"nome_torneio": nome_torneio}

    def mostrar_luta_usuario(self, nome_torneio, boxeador_um, boxeador_dois):
        print("-"*5, f"SUA PRÓXIMA LUTA DO TORNEIO {nome_torneio}", "-"*5)
        print()
        print(f"CHAVE = {boxeador_um.nome}", "vs", f"{boxeador_dois.nome}")
        print(f"{'-'*20} {'-'*20}")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def mostrar_chaveamento(self, nome_torneio, boxeador1, boxeador2, numero_fase=1):
        if numero_fase == 1:
            numero_fase = "final"
        elif numero_fase == 2:
            numero_fase = "semi-final"
        elif numero_fase == 4:
            numero_fase = "quartas-de-final"
        print("-"*5, f"CHAVEAMENTO DO TORNEIO {nome_torneio}", "-"*5)
        print(f"CHAVE {numero_fase} = {boxeador1.nome}", "vs", f"{boxeador2.nome}")
        print()

    def mostrar_torneio(self, nome_torneio, numero_lutadores):
        print()
        print("-"*5, f"TORNEIO {nome_torneio}", "-"*5)
        print()
        print(f"Numero de lutadores: {numero_lutadores}")
        print()

    def tela_opcoes(self):
        print()
        print('-------- ░▒▓█ PUNCH CLUB TORNEIO █▓▒░ ----------',)
        print('Escolha sua opção:')
        print('(1) Cadastrar Torneio')
        print('(2) Alterar Torneio')
        print('(3) Mostrar Torneio')
        print('(0) Retornar')
        print()
        opcao = self.le_num_inteiro("Informe a sua escolha: ", [0, 1, 2, 3])
        return opcao
