from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg

class TelaTorneio(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.inicia_tela_opcoes()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostrar_mensagem(self, mensagem):
        sg.popup('', mensagem)

    def cadastrar_torneio(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CADASTRO DE TORNEIO █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('  ')],
                    [sg.Text('Nome do torneio: ', size=(15, 1)), sg.InputText('', key='nome_torneio')],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]                ]
            )]
        ]
        self.__window = sg.Window('Cadastro Torneio').Layout(layout)

        button, values = self.open()
        nome_torneio = values['nome_torneio']

        self.close()
        return {"nome_torneio": nome_torneio}

    def mostrar_chaveamento(self, nome_torneio, boxeador1, boxeador2):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text(f'⣿⣿⣿ CHAVEAMENTO DO TORNEIO {nome_torneio} ⣿⣿⣿', font=('Lucida', 25, 'bold'))],
                    [sg.Text('  ')],
                    [sg.Text(f'CHAVE = {boxeador1.nome} vs {boxeador2.nome}', size=(15, 1))],
                    [sg.Text('  ')],
                    [sg.Cancel('Voltar')]]
            )]
        ]
        self.__window = sg.Window('mostrar chaveamento').Layout(layout)

    def mostrar_torneio(self, nome_torneio):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ TORNEIO CADASTRADO █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('  ')],
                    [sg.Text(f'Nome do torneio: {nome_torneio}', size=(15, 1))],
                    [sg.Text('   ')],
                    [sg.Cancel('Voltar')]],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('mostrar torneio').Layout(layout)

    def tela_opcoes(self):
        self.inicia_tela_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def inicia_tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ PUNCH CLUB TORNEIO █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('CADASTRAR TORNEIO', size=(20, 2), key='1', button_color=('white', 'black'),
                               border_width=0,font=("Lucida", 12, 'bold'))],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de boxeadores').Layout(layout)

    def obtem_cpf(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text(' ░▒▓█ SELECIONAR BOXEADOR █▓▒░ ', font=("Lucida", 25))],
            [sg.Text('Digite o CPF do boxeador que deseja selecionar:', font=("Lucida", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona boxeador').Layout(layout)

        button, values = self.open()
        cpf = self.le_num_inteiro(values['cpf'])
        self.close()

        return cpf

    def listar_torneios(self, dados_torneio):
        string_torneio = ""
        for torneio in dados_torneio:
            string_torneio = string_torneio + "ID: " + str(torneio["id"]) + '\n'
            string_torneio = string_torneio + "NOME DO TORNEIO: " + torneio["nome_torneio"] + '\n'
            string_torneio = string_torneio + "JOGADOR: " + torneio["nome"] + '\n'
            string_torneio = string_torneio + '\n'
        sg.Popup('░▒▓█ LISTA DE TORNEIOS █▓▒░', string_torneio)
