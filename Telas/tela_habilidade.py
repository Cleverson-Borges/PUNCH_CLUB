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

    def mostrar_mensagem(self, mensagem, auto_close_duration=5):
        layout = [
            [sg.Text(mensagem, font=('Helvetica', 16), justification='center')],
            [sg.Button('OK', size=(10, 1), pad=((200, 0), 3), key='-OK-')]
        ]

        window = sg.Window('Mensagem', layout, finalize=True)

        event, values = window.read(timeout=auto_close_duration * 1000)

        window.close()

    def tela_tipo(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('   ░▒▓█ SELEÇÃO DE HABILIDADES █▓▒░   ', font=("Lucida", 25, 'bold'))],
                    [sg.Text('                                      ', font=("Lucida", 15, 'bold'))],
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
        self.__window = sg.Window('Selecionar de Habilidades').Layout(layout)


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

    def mostrar_habilidade_ataque(self, dados_ataque):
        string_hab_ataque = ""
        for habilidade in dados_ataque:
            string_hab_ataque = string_hab_ataque + "ID: " + str(habilidade["id"]) + '\n'
            string_hab_ataque = string_hab_ataque + "NOME: " + habilidade["nome"] + '\n'
            string_hab_ataque = string_hab_ataque + "DESCRIÇÃO: " + habilidade["descricao"] + '\n'
            string_hab_ataque = string_hab_ataque + "CUSTO DE STAMINA: " + str(habilidade["custo"]) + '\n'
            string_hab_ataque = string_hab_ataque + "DANO DA HABILIDADE: " + str(habilidade["dano"]) + '\n'
            string_hab_ataque = string_hab_ataque + '\n'

        sg.Popup('░▒▓█ LISTA DE HABILIDADES DE ATAQUE █▓▒░', string_hab_ataque)

    def mostrar_habilidade_defesa(self, dados_defesa):
        string_hab_defesa = ""
        for habilidade in dados_defesa:
            string_hab_defesa = string_hab_defesa + "ID: " + str(habilidade["id"]) + '\n'
            string_hab_defesa = string_hab_defesa + "NOME: " + habilidade["nome"] + '\n'
            string_hab_defesa = string_hab_defesa + "DESCRIÇÃO: " + habilidade["descricao"] + '\n'
            string_hab_defesa = string_hab_defesa + "CUSTO DE STAMINA: " + str(habilidade["custo"]) + '\n'
            string_hab_defesa = string_hab_defesa + "TAXA DE DEFESA: " + str(habilidade["taxa_defesa"]) + '\n'
            string_hab_defesa = string_hab_defesa + '\n'

        sg.Popup('░▒▓█ LISTA DE HABILIDADES DE DEFESA █▓▒░', string_hab_defesa)

    def mostrar_habilidade_esquiva(self, dados_esquiva):
        string_hab_esquiva = ""
        for habilidade in dados_esquiva:
            string_hab_esquiva = string_hab_esquiva + "ID: " + str(habilidade["id"]) + '\n'
            string_hab_esquiva = string_hab_esquiva + "NOME: " + habilidade["nome"] + '\n'
            string_hab_esquiva = string_hab_esquiva + "DESCRIÇÃO: " + habilidade["descricao"] + '\n'
            string_hab_esquiva = string_hab_esquiva + "CUSTO DE STAMINA: " + str(habilidade["custo"]) + '\n'
            string_hab_esquiva = string_hab_esquiva + "TAXA DE ESQUIVA: " + str(habilidade["taxa_esquiva"]) + '\n'
            string_hab_esquiva = string_hab_esquiva + '\n'

        sg.Popup('░▒▓█ LISTA DE HABILIDADES DE ESQUIVA █▓▒░', string_hab_esquiva)

    def obtem_id_ataque(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('=== Seleção de habilidades ataque ===', font=("Lucida", 25))],
            [sg.Text('Digite o ID da habilidade que deseja adicionar ao seu boxeador:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('id', key='id_ataque')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('id ataque').Layout(layout)

        button, values = self.open()
        identificador = self.le_num_inteiro_entre(values['identificador'], 1, 3)
        self.close()
        return identificador

    def obtem_id_defesa(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('=== Seleção de habilidades defesa ===', font=("Lucida", 25))],
            [sg.Text('Digite o ID da habilidade que deseja adicionar ao seu boxeador:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('id', key='id_defesa')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('id defesa').Layout(layout)

        button, values = self.open()
        identificador = self.le_num_inteiro_entre(values['identificador'], 4, 6)
        self.close()
        return identificador

    def obtem_id_esquiva(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('=== Seleção de habilidades esquiva ===', font=("Lucida", 25))],
            [sg.Text('Digite o ID da habilidade que deseja adicionar ao seu boxeador:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('id', key='id_esquiva')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('id esquiva').Layout(layout)

        button, values = self.open()
        identificador = self.le_num_inteiro_entre(values['identificador'], 7, 9)
        self.close()

        return identificador
