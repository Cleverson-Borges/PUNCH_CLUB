from Telas.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaCentral(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def print_mensagem(self, mensagem):
        sg.ChangeLookAndFeel('DarkTanBlue')
        sg.PopupNoButtons('', mensagem, auto_close=True, auto_close_duration=5, location=(600, 300))

    def close(self):
        self.__window.Close()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        if button == '0':
            opcao = 0

        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('   ░▒▓█ PUNCH CLUB █▓▒░   ', font=("Lucida", 25, 'bold'))],
                    [sg.Text('                          ', font=("Lucida", 15, 'bold'))],
                    [sg.Button('CADASTRO DE BOXEADOR', size=(23, 2), key='1', button_color=('white', 'black'),
                               border_width=0,font=("Lucida", 12, 'bold'))],
                    [sg.Button('CADASTRO DE TORNEIO', size=(23, 2), key='2', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Text('                          ')],
                    [sg.Button('  ░▓ START GAME ▓░   ', size=(25, 3), key='3', button_color=('green'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Text('                          ')],
                    [sg.Cancel('SAIR', size=(20, 2), button_color=('red'), key='0', font=("Lucida", 12, 'bold'))],
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de contas').Layout(layout)
