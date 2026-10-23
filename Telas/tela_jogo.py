from Telas.tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg
from Telas import exibicao


class TelaJogo(TelaAbstrata):
    def __init__(self):
        sg.theme('DarkTanBlue')
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def obtem_id_torneio(self, lista_ids_validos):
        sg.ChangeLookAndFeel('DarkTanBlue')
        layout = [
            [sg.Text(' ░▒▓█ SELECIONAR ID TORNEIO █▓▒░ ', font=("Lucida", 25))],
            [sg.Text('Digite o ID do torneio que deseja entrar:', font=("Lucida", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Seleciona id do torneio').Layout(layout)

        button, values = self.open()
        self.close()
        # Retorna o id escolhido, ou None se o usuário voltar.
        if button != 'Confirmar':
            return None
        return self.le_num_inteiro(values['id'], lista_ids_validos)


    def tela_luta_padrao(self, vida1, vida2, stamina1, stamina2, nacionalidade1, nacionalidade2, nome1, nome2, apelido1, apelido2, round, total_rounds, nome_fase=''):

        imagens = exibicao.imagens_luta()
        layout = [
            [sg.Image(data=imagens[0], key='-IMAGE-')],
            [sg.Button('LUTAR', key='LUTAR', size=(20, 2), button_color=('white', 'blue')),
             sg.Button('SAIR', key='SAIR', size=(20, 2), button_color=('black', 'pink'))],
            [sg.Text(f'{vida1} HP   {stamina1} ST', size=(40, 2), justification='left', expand_x=True,
                     background_color='black', font=('Helvetica', 14, 'bold'), text_color='white'),
             sg.Text(f'{vida2} HP   {stamina2} ST', size=(40, 2), justification='right', expand_x=True,
                     background_color='black', font=('Helvetica', 14, 'bold'), text_color='white')],
            [sg.Text(apelido1, size=(20, 2), justification='left', expand_x=True,
                     background_color='black', font=('Helvetica', 14, 'bold'), text_color='white'),
             sg.Text(nome1, size=(20, 2), justification='left', expand_x=True,
                     background_color='black', font=('Helvetica', 14, 'bold'), text_color='white'),
             sg.Text(apelido2, size=(20, 2), justification='right', expand_x=True,
                     background_color='black', font=('Helvetica', 14, 'bold'), text_color='white')
             , sg.Text(nome2, size=(20, 2), justification='right', expand_x=True,
                       background_color='black', font=('Helvetica', 14, 'bold'), text_color='white')],
            [sg.Text(nacionalidade1, background_color='black', justification='left',
                     font=('Helvetica', 14, 'bold'), text_color='white', expand_x=True),
             sg.Text(nacionalidade2, background_color='black', justification='right',
                     font=('Helvetica', 14, 'bold'), text_color='white', expand_x=True)],
            [sg.Text(f'{nome_fase}   Round {round} de {total_rounds}', size=(40, 2), justification='center', expand_x=True,
                    background_color='lightgreen', font=('Helvetica', 14, 'bold'), text_color='black')]
        ]

        window = sg.Window('Tela de Luta', layout, finalize=True)
        image_elem = window['-IMAGE-']

        while True:
            for imagem in imagens:
                image_elem.update(data=imagem)
                event, values = window.read(timeout=200)
                if event == sg.WINDOW_CLOSED or event == 'SAIR':
                    window.close()
                    return False
                if event == 'LUTAR':
                    window.close()
                    return True

    def tela_luta_escolha_habilidade(self, vida1, vida2, stamina1, stamina2, mensagem_habilidade_escolhida, habilidades_usuario):

        imagens = exibicao.imagens_luta()
        layout = [
            [sg.Image(data=imagens[0], key='-IMAGE-')],
            [sg.Button('DESISTIR', key='SAIR', size=(10, 2), button_color=('black', 'pink'))],
            [sg.Text(f'{vida1} HP   {stamina1} ST', size=(10, 1), justification='left', expand_x=True,
                     background_color='black', font=('Helvetica', 12), text_color='white'),
             sg.Text(f'{vida2} HP   {stamina2} ST', size=(10, 1), justification='right', expand_x=True,
                     background_color='black', font=('Helvetica', 12), text_color='white')],
            [sg.Text(f'{mensagem_habilidade_escolhida}', size=(10, 1), justification='center', expand_x=True,
                        background_color='black', font=('Helvetica', 14, 'bold'), text_color='white')]
            ]
        lista_habilidades_usuario = []
        if all(habilidade.custo > stamina1 for habilidade in habilidades_usuario):
            layout.append([sg.Button('DESCANSAR\n(recupera stamina, sem ação)', key='DESCANSAR', size=(20, 2),
                                     button_color=('black', 'lightgreen'))])
            lista_habilidades_usuario.append('DESCANSAR')
        for habilidade in habilidades_usuario:
            if habilidade.tipo == 'Ataque':
                botao_habilidade = sg.Button(f'{habilidade.nome}\n(Custo: {habilidade.custo}, Dano: {habilidade.dano})',
                                             key=habilidade.id,
                                             size=(20, 2),
                                             disabled=habilidade.custo > stamina1,
                                             button_color=('black', 'white'))

                layout.append([botao_habilidade])
                lista_habilidades_usuario.append(habilidade.id)
            if habilidade.tipo == 'Defesa':
                botao_habilidade = sg.Button(f'{habilidade.nome}\n(Custo: {habilidade.custo}, Defesa: {habilidade.taxa_defesa})',
                                             key=habilidade.id,
                                             size=(20, 2),
                                             disabled=habilidade.custo > stamina1,
                                             button_color=('black', 'white'))

                layout.append([botao_habilidade])
                lista_habilidades_usuario.append(habilidade.id)
            if habilidade.tipo == 'Esquiva':

                botao_habilidade = sg.Button(f'{habilidade.nome}\n(Custo: {habilidade.custo}, Esquiva: {habilidade.taxa_esquiva})',
                                             key=habilidade.id,
                                             size=(20, 2),
                                             disabled=habilidade.custo > stamina1,
                                             button_color=('black', 'white'))

                layout.append([botao_habilidade])
                lista_habilidades_usuario.append(habilidade.id)

        window = sg.Window('Tela de Luta', layout, finalize=True)
        image_elem = window['-IMAGE-']

        while True:
            for imagem in imagens:
                image_elem.update(data=imagem)
                event, values = window.read(timeout=200)
                if event == sg.WINDOW_CLOSED or event == 'SAIR':
                    window.close()
                    return False
                for habilidade in lista_habilidades_usuario:
                    if event == habilidade:
                        window.close()
                        return habilidade


    def close(self):
        self.__window.Close()

    def mostra_informacoes_luta_usuario(self, dano_total, habilidades_usadas):
        layout = [
            [sg.Text('-------------- RELATÓRIO FINAL DA LUTA --------------')],
            [sg.Text(f"Você causou {dano_total} de dano")],
            [sg.Text(f"Você usou {habilidades_usadas} habilidades")],
            [sg.Text('-----------------------------------------------------')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Relatório Final', layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == 'OK':
                break

        window.close()

    def mostrar_mensagem(self, mensagem, auto_close_duration=5):
        layout = [
            [sg.Text(mensagem, font=('Helvetica', 16), justification='center')],
            [sg.Button('OK', size=(10, 1), pad=((200, 0), 3), key='-OK-')]
        ]

        window = sg.Window('Mensagem', layout, finalize=True)

        event, values = window.read(timeout=auto_close_duration * 1000)

        window.close()

    def mostrar_campeao(self, boxeador_campeao, nome_torneio):

        layout = [
            [sg.Image(data=exibicao.imagem_campeao(), key='-IMAGE-')],
            [sg.Button('SAIR', key='SAIR', size=(20, 2), button_color=('black', 'pink'))],
            [sg.Text(f'Parabéns {boxeador_campeao.nome}! Você é o campeão do {nome_torneio}!', background_color='black', justification='right',
                     font=('Helvetica', 14, 'bold'), text_color='white', expand_x=True)]
        ]

        window = sg.Window('Campeão', layout, finalize=True)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'SAIR':
                window.close()
                return False
