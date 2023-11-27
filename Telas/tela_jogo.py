from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg
import time
import os
import Imagens.base_64_imagens


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
        id = self.le_num_inteiro(values['id'], lista_ids_validos)
        self.close()

        for valor in values:
            if button == 'Voltar':
                self.close()
                return 0
            if values[valor] == '':
                self.close()
                return False
            if button == 'Confirmar':
                return int(id)


    def tela_luta_padrao(self, vida1, vida2, stamina1, stamina2, nacionalidade1, nacionalidade2, nome1, nome2, apelido1, apelido2, round,game_start=False):

        layout = [
            [sg.Image(key='-IMAGE-')],
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
            [sg.Text(f'Round {round} de 3', size=(40, 2), justification='center', expand_x=True,
                    background_color='lightgreen', font=('Helvetica', 14, 'bold'), text_color='black')]
        ]

        window = sg.Window('Tela de Luta', layout, no_titlebar=True, grab_anywhere=True,
                           keep_on_top=True, location=(200, 000), finalize=True)        
        image_elem = window['-IMAGE-']

        images_base64 = [Imagens.base_64_imagens.boxe_image_base_64,
                         Imagens.base_64_imagens.boxe_image_2_base_64,
                         Imagens.base_64_imagens.boxe_image_3_base_64
                         ]

        while True:
            for image_base64 in images_base64:
                image_elem.update(data=image_base64)
                event, values = window.read(timeout=200)
                if event == sg.WINDOW_CLOSED or event == 'SAIR':
                    window.close()
                    return False
                if event == 'LUTAR':
                    if not game_start:
                        window.close()
                        return True
                    else:
                        window.close()

    def tela_luta_escolha_habilidade(self, vida1, vida2, stamina1, stamina2, mensagem_habilidade_escolhida, habilidades_usuario):

        layout = [
            [sg.Image(key='-IMAGE-')],
            [sg.Button('SAIR', key='SAIR', size=(10, 2), button_color=('black', 'pink'))],
            [sg.Text(f'{vida1} HP   {stamina1} ST', size=(10, 1), justification='left', expand_x=True,
                     background_color='black', font=('Helvetica', 12), text_color='white'),
             sg.Text(f'{vida2} HP   {stamina2} ST', size=(10, 1), justification='right', expand_x=True,
                     background_color='black', font=('Helvetica', 12), text_color='white')],
            [sg.Text(f'{mensagem_habilidade_escolhida}', size=(10, 1), justification='center', expand_x=True,
                        background_color='black', font=('Helvetica', 14, 'bold'), text_color='white')]
            ]
        lista_habilidades_usuario = []
        for habilidade in habilidades_usuario:
            if habilidade.tipo == 'Ataque':
                botao_habilidade = sg.Button(f'{habilidade.nome}\n(Custo: {habilidade.custo}, Dano: {habilidade.dano})',
                                             key=habilidade.id,
                                             size=(20, 2),
                                             button_color=('black', 'white'))

                layout.append([botao_habilidade])
                lista_habilidades_usuario.append(habilidade.id)
            if habilidade.tipo == 'Defesa':
                botao_habilidade = sg.Button(f'{habilidade.nome}\n(Custo: {habilidade.custo}, Defesa: {habilidade.taxa_defesa})',
                                             key=habilidade.id,
                                             size=(20, 2),
                                             button_color=('black', 'white'))

                layout.append([botao_habilidade])
                lista_habilidades_usuario.append(habilidade.id)
            if habilidade.tipo == 'Esquiva':

                botao_habilidade = sg.Button(f'{habilidade.nome}\n(Custo: {habilidade.custo}, Esquiva: {habilidade.taxa_esquiva})',
                                             key=habilidade.id,
                                             size=(20, 2),
                                             button_color=('black', 'white'))

                layout.append([botao_habilidade])
                lista_habilidades_usuario.append(habilidade.id)

        window = sg.Window('Tela de Luta', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True, finalize=True)
        image_elem = window['-IMAGE-']

        images_base64 = [Imagens.base_64_imagens.boxe_image_base_64,
                         Imagens.base_64_imagens.boxe_image_2_base_64,
                         Imagens.base_64_imagens.boxe_image_3_base_64
                         ]

        while True:
            for image_base64 in images_base64:
                image_elem.update(data=image_base64)
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
            [sg.Text(f"Você usou {habilidades_usadas - 1} habilidades")],
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

    def mostrar_campeao(self, boxeador_campeao):

        layout = [
            [sg.Image(key='-IMAGE-')],
            [sg.Button('SAIR', key='SAIR', size=(20, 2), button_color=('black', 'pink'))],
            [sg.Text(f'Parabéns {boxeador_campeao.nome}! Você mereceu!', background_color='black', justification='right',
                     font=('Helvetica', 14, 'bold'), text_color='white', expand_x=True)]
        ]

        window = sg.Window('Tela de Luta', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True, finalize=True)
        image_elem = window['-IMAGE-']

        imagem_campeao = Imagens.base_64_imagens.boxe_image_4_base_64,

        while True:
            image_elem.update(data=imagem_campeao)
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'SAIR':
                window.close()
                return False
