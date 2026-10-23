from Telas.tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaBoxeador(TelaAbstrata):
    def __init__(self):
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def cadastrar_boxeador(self):
        # Retorna o dicionário com os dados do boxeador, ou None se o usuário voltar.
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
                    [sg.Text('░▒▓█ CADASTRAMENTO DE NOVO BOXEADOR █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                    [sg.Text('Apelido:', size=(15, 1)), sg.InputText('', key='apelido')],
                    [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade'), sg.Text('(min: 18 max: 100)')],
                    [sg.Text('Peso:', size=(15, 1)), sg.InputText('', key='peso'), sg.Text('(min: 35kg max: 150.7kg)')],
                    [sg.Text('Altura:', size=(15, 1)), sg.InputText('', key='altura'), sg.Text('(min: 1.20m max: 2.30m)')],
                    [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('', key='nacionalidade'),
                     sg.Text('(3 letras iniciais)')],
                    [sg.Button('Cadastrar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Cadastamento boxeador').Layout(layout)

        button, values = self.open()
        self.close()
        if button != 'Cadastrar':
            return None

        nome = self.le_str_nao_vazia(values['nome'], 'nome')
        apelido = self.le_str_nao_vazia(values['apelido'], 'apelido') if nome is not None else None
        idade = self.le_num_inteiro_entre(values['idade'], 18, 100) if apelido is not None else None
        peso = self.le_num_float_entre(values['peso'], 35.0, 150.7) if idade is not None else None
        altura = self.le_num_float_entre(values['altura'], 1.20, 2.30) if peso is not None else None
        nacionalidade = self.le_str_valida(values['nacionalidade']) if altura is not None else None
        if nacionalidade is None:
            return None

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
        self.close()
        if button in ('1', '2', '3', '4', '5', '6'):
            return int(button)
        return 0

    def mostrar_mensagem(self, mensagem):
        sg.popup('', mensagem)

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

    def mostra_boxeador(self, dados_boxeador):
        string_todos_boxeadores = ""
        for boxeador in dados_boxeador:
            string_todos_boxeadores = string_todos_boxeadores + "NOME DO BOXEADOR: " + boxeador["nome"] + '\n'
            string_todos_boxeadores = string_todos_boxeadores + "CPF DO BOXEADOR: " + str(boxeador["cpf"]) + '\n'
            string_todos_boxeadores = string_todos_boxeadores + "APELIDO: " + boxeador["apelido"] + '\n'
            string_todos_boxeadores = string_todos_boxeadores + "INSCRIÇÃO: " + str(boxeador["numero_inscricao"]) + '\n'
            string_todos_boxeadores = string_todos_boxeadores + "CONTROLE: " + ("CPU" if boxeador["CPU"] else "Você") + '\n'
            string_todos_boxeadores = string_todos_boxeadores + '\n'

        sg.popup_scrolled(string_todos_boxeadores, title='░▒▓█ LISTA DE BOXEADORES █▓▒░', size=(60, 25))

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
            string_todas_caracteristicas = string_todas_caracteristicas + f"IMC: {caracteristica['imc']:.1f}" + '\n'
            string_todas_caracteristicas = string_todas_caracteristicas + "BÔNUS DO IMC NA LUTA: " + caracteristica["bonus_imc"] + '\n'

        sg.Popup('░▒▓█ LISTA DE CARACTERISTICAS DO BOXEADOR █▓▒░', string_todas_caracteristicas)

    def close(self):
        self.__window.Close()
