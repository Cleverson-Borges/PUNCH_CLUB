from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg


class TelaHabilidade(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()


    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def print_mensagem(self, mensagem):
        sg.popup('', mensagem)

    def tela_tipo(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('   ░▒▓█ SELEÇÃO DE HABILIDADES █▓▒░   ', font=("Lucida", 25, 'bold'))],
                    [sg.Text('                          ', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Habilidades de Ataque', size=(20, 2), key='1', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Habilidades de Defesa', size=(20, 2), key='2', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('Habilidades de Esquiva', size=(20, 2), key='3', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Cancel('SAIR', size=(20, 2), key='4', font=("Lucida", 12, 'bold'))],
                ],
                element_justification='center'
            )]
        ]

    def selecionar_tipo(self):
        self.tela_tipo()
        button, values = self.__window.Read()
        opcao = 0
        if button == '1':
            opcao = 1
        if button == '2':
            opcao = 2
        if button == '3':
            opcao = 3
        if button == '4':
            opcao = 4

        self.close()

        return opcao

    def mostrar_habilidade_ataque(self, habilidade):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('⣿⣿⣿ HABILIDADES DE ATAQUE ⣿⣿⣿', font=('Lucida', 25))],
                    [sg.Text(f'ID da habilidade:   {habilidade.id}')],
                    [sg.Text(f'Nome:               {habilidade.nome}')],
                    [sg.Text(f'Descrição :         {habilidade.descricao}')],
                    [sg.Text(f'Custo de Stamina:   {habilidade.stamina}')],
                    [sg.Text(f'Dano da habilidade: {habilidade.dano}')],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                              font=('Lucida', 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Habilidades Ataque').Layout(layout)

    def mostrar_habilidade_defesa(self, habilidade):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('⣿⣿⣿ HABILIDADES DE DEFESA ⣿⣿⣿', font=('Lucida', 25))],
                    [sg.Text(f'ID da habilidade: {habilidade.id}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Nome:             {habilidade.nome}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Descrição :       {habilidade.descricao}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Custo de Stamina: {habilidade.stamina}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Taxa de Defesa:   {habilidade.taxa_defesa}', font=('Lucida', 15, 'bold'))],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                              font=('Lucida', 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Habilidades Defesa').Layout(layout)

    def mostrar_habilidade_esquiva(self, habilidade):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('⣿⣿⣿ HABILIDADES DE ESQUIVA ⣿⣿⣿', font=('Lucida', 25))],
                    [sg.Text(f'ID da habilidade: {habilidade.id}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Nome:             {habilidade.nome}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Descrição :       {habilidade.descricao}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Custo de Stamina: {habilidade.stamina}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Taxa de Esquiva:  {habilidade.taxa_esquiva}', font=('Lucida', 15, 'bold'))],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                              font=('Lucida', 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Habilidades Esquiva').Layout(layout)

    def obtem_id_ataque(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('=== Seleção de habilidades ===', font=("Lucida", 25))],
            [sg.Text('Digite o ID da habilidade que deseja adicionar ao seu boxeador:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('id', key='id_ataque')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('id ataque').Layout(layout)

        button, values = self.open()
        identificador = values['identificador']
        self.close()
        return identificador

    def obtem_id_defesa(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('=== Seleção de habilidades ===', font=("Lucida", 25))],
            [sg.Text('Digite o ID da habilidade que deseja adicionar ao seu boxeador:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('id', key='id_defesa')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('id defesa').Layout(layout)

        button, values = self.open()
        identificador = values['identificador']
        self.close()
        return identificador

    def obtem_id_esquiva(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('=== Seleção de habilidades ===', font=("Lucida", 25))],
            [sg.Text('Digite o ID da habilidade que deseja adicionar ao seu boxeador:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('id', key='id_esquiva')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('id esquiva').Layout(layout)

        button, values = self.open()
        identificador = values['identificador']
        self.close()
        return identificador