from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg


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

    def cadastrar_torneio(self):
        print("-"*15, "CADASTRAMENTO DE TORNEIO", "-"*15)
        print()
        nome_torneio = input(str("Informe o nome que deseja dar ao torneio PUNCH CLUB: "))
        return nome_torneio

    def alterar_torneio(self):
        print("-"*15, "ALTERAR NOME DO TORNEIO", "-"*15)
        print()
        nome_torneio = input(str("Informe o novo nome que deseja dar ao torneio PUNCH CLUB: "))
        print()
        return {"nome_torneio": nome_torneio}

    def mostrar_luta_usuario(self, nome_torneio, boxeador_um, boxeador_dois):
        layout = [
            [sg.Text(f"SUA LUTA DA NOITE É {nome_torneio}", font=('Helvetica', 16), justification='center')],
            [sg.Text()],
            [sg.Text(f"= {boxeador_um.nome} vs {boxeador_dois.nome}", font=('Helvetica', 14), justification='center')],
            [sg.Text('-' * 20 + ' ' * 20 + '-' * 20, justification='center')],
            [sg.Button('OK')]
        ]

        window = sg.Window(f'Luta do Torneio {nome_torneio}', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'OK':
                break

        window.close()

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

    def mostrar_torneio(self, nome_torneio, numero_lutadores, id_torneio):
        print()
        print("-"*5, f"TORNEIO {nome_torneio}", "-"*5)
        print(f"ID DO TORNEIO: {id_torneio}")
        print()
        print(f"Numero de lutadores: {numero_lutadores}")
        print()

    def tela_opcoes(self):
        print()
        print('-------- ░▒▓█ PUNCH CLUB TORNEIO █▓▒░ ----------',)
        print('Escolha sua opção:')
        print('(1) Cadastrar Torneio')
        print('(0) Retornar')
        print()
        opcao = self.le_num_inteiro("Informe a sua escolha: ", [0, 1])
        return opcao

    def obtem_cpf(self):
        cpf = input("Informe o cpf do seu boxeador: ")
        return int(cpf)

    def obtem_id_torneio(self):
        id_torneio = input("Informe o id do torneio: ")
        return int(id_torneio)