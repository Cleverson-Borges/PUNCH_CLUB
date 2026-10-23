from Telas.tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaTorneio(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostrar_mensagem(self, mensagem):
        sg.popup('', mensagem)

    def cadastrar_torneio(self, numeros_lutadores_validos):
        # Retorna o nome e o número de lutadores, ou None se o usuário cancelar.
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CADASTRO DE TORNEIO █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('  ')],
                    [sg.Text('Nome do torneio: ', size=(18, 1)), sg.InputText('', key='nome_torneio')],
                    [sg.Text('Número de lutadores: ', size=(18, 1)),
                     sg.Combo(list(numeros_lutadores_validos), default_value=numeros_lutadores_validos[0],
                              key='numero_lutadores', readonly=True)],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]
            )]
        ]
        self.__window = sg.Window('Cadastro Torneio').Layout(layout)

        button, values = self.open()
        self.close()
        if button != 'Confirmar':
            return None
        nome_torneio = self.le_str_nao_vazia(values['nome_torneio'], 'nome do torneio')
        if nome_torneio is None:
            return None
        return {"nome_torneio": nome_torneio, "numero_lutadores": int(values['numero_lutadores'])}

    def mostrar_chaveamento(self, nome_torneio, fases):
        # fases: lista de {'nome': str, 'lutas': [{'boxeador_um', 'boxeador_dois', 'vencedor'}]}
        texto = ''
        for fase in fases:
            texto += f"=== {fase['nome'].upper()} ===\n"
            for luta in fase['lutas']:
                resultado = f"  →  vencedor: {luta['vencedor']}" if luta['vencedor'] else ''
                texto += f"{luta['boxeador_um']} vs {luta['boxeador_dois']}{resultado}\n"
            texto += '\n'
        sg.popup_scrolled(texto, title=f'CHAVEAMENTO DO TORNEIO {nome_torneio}', size=(70, 20))

    def mostrar_luta_usuario(self, nome_torneio, nome_fase, boxeador_um, boxeador_dois):
        layout = [
            [sg.Text(f"SUA LUTA DA NOITE NO TORNEIO {nome_torneio}", font=('Helvetica', 16), justification='center')],
            [sg.Text(nome_fase.upper(), font=('Helvetica', 14, 'bold'), justification='center')],
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

    def tela_opcoes(self):
        self.inicia_tela_opcoes()
        button, values = self.__window.Read()
        self.close()
        if button in ('1', '2'):
            return int(button)
        return 0

    def inicia_tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ PUNCH CLUB TORNEIO █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('CADASTRAR TORNEIO', size=(20, 2), key='1', button_color=('white', 'black'),
                               border_width=0,font=("Lucida", 12, 'bold'))],
                    [sg.Button('LISTAR TORNEIOS', size=(20, 2), key='2', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de torneios').Layout(layout)

    def obtem_cpf(self):
        # Retorna o CPF digitado, ou None se o usuário voltar.
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text(' ░▒▓█ SELECIONAR BOXEADOR █▓▒░ ', font=("Lucida", 25))],
            [sg.Text('Digite o CPF do boxeador que deseja selecionar:', font=("Lucida", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona boxeador').Layout(layout)

        button, values = self.open()
        self.close()
        if button != 'Confirmar':
            return None
        return self.le_num_inteiro(values['cpf'])

    def obtem_id_chaveamento(self, lista_ids_validos):
        # Retorna o id do torneio cujo chaveamento será exibido, ou None se o usuário voltar.
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text('Digite o ID do torneio para ver o chaveamento:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Ver chaveamento').Layout(layout)

        button, values = self.open()
        self.close()
        if button != 'Confirmar':
            return None
        return self.le_num_inteiro(values['id'], lista_ids_validos)

    def listar_torneios(self, dados_torneio):
        string_torneio = ""
        for torneio in dados_torneio:
            string_torneio = string_torneio + "ID: " + str(torneio["id"]) + '\n'
            string_torneio = string_torneio + "NOME DO TORNEIO: " + torneio["nome_torneio"] + '\n'
            string_torneio = string_torneio + "JOGADOR: " + torneio["nome"] + '\n'
            string_torneio = string_torneio + "LUTADORES: " + str(torneio["numero_lutadores"]) + '\n'
            string_torneio = string_torneio + "PRÓXIMA FASE: " + torneio["fase"] + '\n'
            string_torneio = string_torneio + '\n'
        sg.popup_scrolled(string_torneio, title='░▒▓█ LISTA DE TORNEIOS █▓▒░', size=(60, 20))
