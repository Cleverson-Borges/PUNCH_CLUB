from Telas.tela_central import TelaAbstrata
import PySimpleGUI as sg


class TelaCaracteristica(TelaAbstrata):
    def __init__(self):
        self.__window = None
        pass

    def tela_cadastro_status(self):
        forca = 10
        esquiva = 10
        vida = 100
        defesa = 10
        stamina = 15
        incremento_de_pontos = 3
        incremento_de_vida = 10
        for i in range(10):
            sg.ChangeLookAndFeel('DarkTanBlue')
            layout = [
                [sg.Column(
                    [
                    [sg.Text('=== DISTRIBUIÇÃO DE PONTOS ===', font=("Lucida", 25))],
                    [sg.Text('                                      ', font=("Lucida", 15, 'bold'))],
                    [sg.Text(f'Você tem {10 - i} ponto(s) para distribuir', font=("Lucida", 15, 'bold'))],
                    [sg.Button('FORÇA (+3)', size=(20, 2), key='1', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('ESQUIVA (+3)', size=(20, 2), key='2', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('VIDA (+10)', size=(20, 2), key='3', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('DEFESA (+3)', size=(20, 2), key='4', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                    [sg.Button('STAMINA(+3)', size=(20, 2), key='5', button_color=('white', 'black'),
                               border_width=0, font=("Lucida", 12, 'bold'))],
                        ],
                element_justification='center'
                )]
            ]
            self.__window = sg.Window('=== DISTRIBUIÇÃO DE PONTOS ===').Layout(layout)

            button, values = self.__window.Read()
            if button == 1:
                forca = forca + incremento_de_pontos
            elif button == 2:
                esquiva = esquiva + incremento_de_pontos
            elif button == 3:
                vida = vida + incremento_de_vida
            elif button == 4:
                defesa = defesa + incremento_de_pontos
            elif button == 5:
                stamina = stamina + incremento_de_pontos
            elif button == 0:
                break

        return {'forca': forca,
                'esquiva': esquiva,
                'vida': vida,
                'defesa': defesa,
                'stamina': stamina}
