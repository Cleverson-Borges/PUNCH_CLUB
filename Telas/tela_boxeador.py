from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg


class TelaBoxeador(TelaAbstrata):
    def __init__(self):
        self.tela_opcoes()

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

    def le_num_inteiro_entre(self, mensagem=" ", min_valor=None, max_valor=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if (min_valor is not None and valor_int < min_valor) or (
                        max_valor is not None and valor_int > max_valor):
                    raise ValueError
                return valor_int
            except ValueError:
                print(f"Você deve ter no minímo {min_valor} anos e no maximo {max_valor} anos para poder participar.")

    def le_num_float_entre(self, mensagem=" ", min_valor=None, max_valor=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_float = float(valor_lido)
                if (min_valor is not None and valor_float < min_valor) or (
                        max_valor is not None and valor_float > max_valor):
                    raise ValueError
                return valor_float
            except ValueError:
                print(f"O valor deve estar entre {min_valor} e {max_valor}.")

    def le_str_valida(self, mensagem=" ", strs_validas=None):
        while True:
            valor_lido = input(mensagem)
            if len(valor_lido) == 3:
                if strs_validas and valor_lido not in strs_validas:
                    print("Valor incorreto!")
                    if strs_validas:
                        print("Valores válidos: ", ", ".join(strs_validas))
                else:
                    return valor_lido.upper()
            else:
                print("A string deve conter exatamente 3 letras.")

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def cadastrar_boxeador(self):
        print('Cadastro de boxeador')
        nome = str(input('Nome: '))
        apelido = str(input('Apelido: '))
        idade = self.le_num_inteiro_entre('Idade: ', 18, 100)
        peso = self.le_num_float_entre('Peso: ', 30, 150)
        altura = self.le_num_float_entre('Altura [metros]: ', 1.20, 2.30)
        nacionalidade = self.le_str_valida('Nacionalidade: ')
        print()
        return {'nome': nome,
                'apelido': apelido,
                'idade': idade,
                'peso': peso,
                'altura': altura,
                'nacionalidade': nacionalidade}

    def tela_cadastro_boxeador(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
                    [sg.Text('░▒▓█ CADASTRAMENTO DE NOVO BOXEADOR █▓▒░', font=('Lucida', 25, 'bold'))],
                    [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                    [sg.Text('Apelido:', size=(15, 1)), sg.InputText('', key='apelido')],
                    [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
                    [sg.Text('Peso:', size=(15, 1)), sg.InputText('', key='peso')],
                    [sg.Text('Altura:', size=(15, 1)), sg.InputText('', key='altura')],
                    [sg.Text('Nacionalidade:', size=(15, 1)), sg.InputText('', key='nacionalidade')],
                    [sg.Button('Cadastrar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Cadastamento boxeador').Layout(layout)



    def tela_opcoes(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('░▒▓█ CADASTRO DE BOXEADOR █▓▒░', font=("Lucida", 25, 'bold'))],
                    [sg.Text('Escolha sua opção:', font=("Lucida", 15, 'bold'))],
                    [sg.Button('Incluir boxeador', size=(20, 2), key='1', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Alterar boxeador', size=(20, 2), key='2', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Listar boxeadores', size=(20, 2), key='3', button_color=('white', 'black'), border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Excluir boxeador', size=(20, 2), key='4', button_color=('white', 'black'),
                               border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Listar habilidades boxeador', size=(20, 2), key='5', button_color=('white', 'black'),
                               border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Listar caracteristicas boxeador', size=(20, 2), key='6', button_color=('white', 'black'),
                               border_width=0,
                               font=("Lucida", 12, 'bold'))],
                    [sg.Button('Confirmar', size=(8, 1), button_color=('black', 'green'),
                               font=("Lucida", 12, 'bold')),
                     sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
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

        if button == '0' in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def obtem_cpf(self):
        cpf = self.le_num_inteiro('Por favor, insira o CPF: ')
        print()
        return cpf

    def seleciona_por_cpf(self):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text(' ░▒▓█ SELECIONAR BOXEADOR █▓▒░ ', font=("Lucida", 25))],
            [sg.Text('Digite o CPF do boxeador que deseja selecionar:', font=("Lucida", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('cpf', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona boxeador').Layout(layout)

        button, values = self.open()
        identificador = values['identificador']
        self.close()
        return identificador

    def verifica_boxeador_cpu(self):
        resposta = input('Este é o lutador que você quer jogar? (Responda com S (Sim) ou N (Não): ')
        return resposta

    def mostra_boxeador(self, dados_boxeador):
        print()
        print(f'NOME DO BOXEADOR: {dados_boxeador["nome"]}')
        print(f'CPF: {dados_boxeador["cpf"]}')
        print(f'APELIDO: {dados_boxeador["apelido"]}')
        print(f'IDADE: {dados_boxeador["idade"]} anos')
        print(f'PESO: {dados_boxeador["peso"]} kg')
        print(f'ALTURA: {dados_boxeador["altura"]} m')
        print(f'NACIONALIDADE: {dados_boxeador["nacionalidade"]}')
        print()

    def tela_exibe_boxeadores(self, dados_boxeador):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Column(
                [
                    [sg.Text('⣿⣿⣿ BOXEADORES CREDENCIADOS ⣿⣿⣿', font=('Lucida', 25,))],
                    [sg.Text(f'NOME DO BOXEADOR: {dados_boxeador["nome"]}', font=('Lucida', 15))],
                    [sg.Text(f'CPF: {dados_boxeador["cpf"]}', font=('Lucida', 15))],
                    [sg.Text(f'APELIDO: {dados_boxeador["apelido"]}', font=('Lucida', 15))],
                    [sg.Text(f'IDADE: {dados_boxeador["idade"]} anos', font=('Lucida', 15))],
                    [sg.Text(f'PESO: {dados_boxeador["peso"]} kg', font=('Lucida', 15))],
                    [sg.Text(f'ALTURA: {dados_boxeador["altura"]} m', font=('Lucida', 15))],
                    [sg.Text(f'NACIONALIDADE: {dados_boxeador["nacionalidade"]}', font=('Lucida', 15))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Boxeadores Credenciados').Layout(layout)

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

    def mostrar_caracteristica_boxeador(self, caracteristica):
        sg.ChangeLookAndFeel("DarkTanBlue")
        layout = [
            [sg.Column(
                [
                    [sg.Text('⣿⣿⣿ CARACTERISTICAS ⣿⣿⣿', font=("Lucida", 25, 'bold'))],
                    [sg.Text(f'Stamina: {caracteristica.stamina}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Esquiva: {caracteristica.esquiva}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Vida:    {caracteristica.vida}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Força:   {caracteristica.forca}', font=('Lucida', 15, 'bold'))],
                    [sg.Text(f'Defesa:  {caracteristica.defesa}', font=('Lucida', 15, 'bold'))],
                    [sg.Cancel('Voltar', size=(8, 1), key='0', button_color=('black', 'red'),
                              font=('Lucida', 12, 'bold'))]
                ],
                element_justification='center'
            )]
        ]
        self.__window = sg.Window('Tela Caracteristicas').Layout(layout)

    def close(self):
        self.__window.Close()

    def print_mensagem(self, mensagem):
        sg.popup('', mensagem)
