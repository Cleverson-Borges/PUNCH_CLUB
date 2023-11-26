from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg

class TelaTorneio(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.tela_opcoes()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def print_mensagem(self, mensagem):
        sg.popup('', mensagem)

    def tela_cadastro_torneio(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CADASTRO DE TORNEIO █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('  ')],
                    [sg.Text('Nome do torneio: ', size=(15, 1)), sg.InputText('', key='nome_torneio')],
                    [sg.Text('Numero de lutadores: ', size=(15, 1)), sg.InputText('', key='numero_lutadores')],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]                ]
            )]
        ]
        self.__window = sg.Window('Cadastro Torneio').Layout(layout)

        button, values = self.open()
        nome_torneio = values['nome_torneio']
        numero_lutadores = values['numero_lutadores']

        self.close()
        return {"nome_torneio": nome_torneio, "numero_lutadores": numero_lutadores}

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

        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text(f'⣿⣿⣿ CHAVEAMENTO DO TORNEIO {nome_torneio} ⣿⣿⣿', font=('Lucida', 25, 'bold'))],
                    [sg.Text('  ')],
                    [sg.Text(f'CHAVE {numero_fase} = {boxeador1.nome} vs {boxeador2.nome}', size=(15, 1))],
                    [sg.Text('  ')],
                    [sg.Cancel('Voltar')]]
            )]
        ]
        self.__window = sg.Window('mostrar chaveamento').Layout(layout)

    def mostrar_torneio(self, nome_torneio, numero_lutadores):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ TORNEIO CADASTRADO █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('  ')],
                    [sg.Text(f'Nome do torneio: {nome_torneio}', size=(15, 1))],
                    [sg.Text('   ')],
                    [sg.Text(f'Numero de lutadores: {numero_lutadores}', size=(15, 1))],
                    [sg.Cancel('Voltar')]],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('mostrar torneio').Layout(layout)

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ PUNCH CLUB TORNEIO █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Cadastrar Torneio', size=(20, 2), key='1', button_color=('white', 'black'),
                               border_width=0,font=("Lucida", 12, 'bold'))],
                    [sg.Button('ALTERAR TORNEIO', size=(20, 2), key='2', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('MOSTRAR TORNEIO', size=(20, 2), key='3', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de boxeadores').Layout(layout)

    def init_tela_opcoes(self):
        self.tela_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao
