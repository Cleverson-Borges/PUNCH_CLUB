from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg


class TelaBoxeador(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.tela_opcoes()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def cadastrar_boxeador(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
                    [sg.Text('░▒▓█ CADASTRAMENTO DE NOVO BOXEADOR █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                    [sg.Text('Apelido:', size=(15, 1)), sg.InputText('', key='apelido')],
                    [sg.Text('Idade:', size=(15, 1)), sg.InputText('(min: 18 max: 100)', key='idade')],
                    [sg.Text('Peso:', size=(15, 1)), sg.InputText('(min: 35kg max: 150.7kg)', key='peso')],
                    [sg.Text('Altura:', size=(15, 1)), sg.InputText('(min: 1.20m max: 2.30m)', key='altura')],
                    [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('(3 letras iniciais)', key='nacionalidade')],
                    [sg.Button('Cadastrar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Cadastamento boxeador').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        apelido = values['apelido']
        idade = self.le_num_inteiro_entre(values['idade'], 18, 100)
        peso = self.le_num_float_entre(values['peso'], 35.0, 150.7)
        altura = self.le_num_float_entre(values['altura'], 1.20, 2.20)
        nacionalidade = self.le_str_valida(values['nacionalidade'])

        self.close()
        return {"nome": nome, "apelido": apelido, "idade": idade, "peso": peso, "altura": altura,
                "nacionalidade": nacionalidade}

    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CADASTRO DE BOXEADOR █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Incluir boxeador', size=(20, 2), key='1', button_color=('white', 'black'),
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Alterar boxeador', size=(20, 2), key='2', button_color=('white', 'black'),
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Listar boxeadores', size=(20, 2), key='3', button_color=('white', 'black'),
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Excluir boxeador', size=(20, 2), key='4', button_color=('white', 'black'),
                               border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Listar habilidades boxeador   ', size=(20, 2), key='5', button_color=('white', 'black'),
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Listar caracteristicas boxeador', size=(20, 2), key='6',
                               button_color=('white', 'black'), font=("Lucida", 12, 'bold'))],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                               font=("Lucida", 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Cadastro de contas').Layout(layout)

    def primeira_tela_opcoes(self):
        self.tela_opcoes()
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
        if button == '5':
            opcao = 5
        if button == '6':
            opcao = 6
        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def mostrar_mensagem(self, mensagem):
        sg.popup('', mensagem)

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

    def verifica_boxeador_cpu(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text(' ░▒▓█ SELECIONAR BOXEADOR █▓▒░ ', font=("Lucida", 25))],
            [sg.Text('Este é o lutador que você quer jogar? (S/N): ', size=(15, 1)), sg.InputText('', key='resposta')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona boxeador').Layout(layout)
        resposta = input('Este é o lutador que você quer jogar? (Responda com S (Sim) ou N (Não): ')
        return resposta

    def mostra_boxeador(self, dados_boxeador):
        string_todos_boxeadores = ""
        for boxeador in dados_boxeador:
            string_todos_boxeadores = string_todos_boxeadores + "NOME DO BOXEADOR: " + boxeador["nome"] + '\n'
            string_todos_boxeadores = string_todos_boxeadores + "CPF DO BOXEADOR: " + str(boxeador["cpf"]) + '\n'
            string_todos_boxeadores = string_todos_boxeadores + "APELIDO: " + boxeador["apelido"] + '\n'
            string_todos_boxeadores = string_todos_boxeadores + '\n'

        sg.Popup('░▒▓█ LISTA DE BOXEADORES █▓▒░', string_todos_boxeadores)

    def lista_habilidades(self, dados_habilidade):
        string_todas_habilidades = ""
        for habilidade in dados_habilidade:
            string_todas_habilidades = string_todas_habilidades + "ID DA HABILIDADE: " + str(habilidade["id"]) + '\n'
            string_todas_habilidades = string_todas_habilidades + "NOME DA HABILIDADE: " + habilidade["nome"] + '\n'
            string_todas_habilidades = string_todas_habilidades + "DESCRIÇÃO DA HABILIDADE: " + habilidade["descricao"] + '\n'
            string_todas_habilidades = string_todas_habilidades + "CUSTO DE STAMINA: " + str(habilidade["custo"]) + '\n'
            if habilidade['tipo'] == 'Ataque':
                string_todas_habilidades = string_todas_habilidades + "DANO DA HABILIDADE: " + str(habilidade["dano"]) + '\n'
            if habilidade['tipo'] == 'Defesa':
                string_todas_habilidades = string_todas_habilidades + "TAXA DE DEFESA: " + str(habilidade["taxa_defesa"]) + '\n'
            if habilidade['tipo'] == 'Esquiva':
                string_todas_habilidades = string_todas_habilidades + "TAXA DE ESQUIVA: " + str(habilidade["taxa_esquiva"]) + '\n'
            string_todas_habilidades = string_todas_habilidades + '\n'

        sg.Popup('░▒▓█ LISTA DE HABILIDADES DO BOXEADOR █▓▒░', string_todas_habilidades)

    def mostrar_caracteristica_boxeador(self, dados_caracteristica):
        string_todas_caracteristicas = ""
        for caracteristica in dados_caracteristica:
            string_todas_caracteristicas = string_todas_caracteristicas + "FORÇA: " + str(caracteristica["forca"]) + '\n'
            string_todas_caracteristicas = string_todas_caracteristicas + "ESQUIVA: " + str(caracteristica["esquiva"]) + '\n'
            string_todas_caracteristicas = string_todas_caracteristicas + "VIDA: " + str(caracteristica["vida"]) + '\n'
            string_todas_caracteristicas = string_todas_caracteristicas + "STAMINA: " + str(caracteristica["stamina"]) + '\n'
            string_todas_caracteristicas = string_todas_caracteristicas + "DEFESA: " + str(caracteristica["defesa"]) + '\n'

            string_todas_caracteristicas = string_todas_caracteristicas + '\n'

        sg.Popup('░▒▓█ LISTA DE CARACTERISTICAS DO BOXEADOR █▓▒░', string_todas_caracteristicas)
    def close(self):
        self.__window.Close()
