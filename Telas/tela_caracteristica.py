from Telas.tela_abstrata import TelaAbstrata
import FreeSimpleGUI as sg


class TelaCaracteristica(TelaAbstrata):
    # Quanto cada ponto distribuído soma em cada característica (regra da documentação)
    INCREMENTOS = {'forca': 1, 'esquiva': 1, 'vida': 2, 'defesa': 1, 'stamina': 1}

    def __init__(self):
        self.__window = None

    def tela_cadastro_status(self):
        valores_iniciais = {'forca': 10, 'esquiva': 10, 'vida': 100, 'defesa': 10, 'stamina': 15}
        return self.tela_distribuir_pontos(10, valores_iniciais, permite_cancelar=True)

    def tela_distribuir_pontos(self, pontos, valores_atuais, permite_cancelar=False):
        # Retorna o dicionário com os novos valores, ou None se o usuário cancelar.
        valores = dict(valores_atuais)
        botoes = {'1': 'forca', '2': 'esquiva', '3': 'vida', '4': 'defesa', '5': 'stamina'}
        rotulos = {'forca': 'FORÇA', 'esquiva': 'ESQUIVA', 'vida': 'VIDA', 'defesa': 'DEFESA', 'stamina': 'STAMINA'}
        pontos_restantes = pontos
        while pontos_restantes > 0:
            sg.ChangeLookAndFeel('DarkTanBlue')
            linhas_botoes = []
            for chave, caracteristica in botoes.items():
                texto = (f'{rotulos[caracteristica]} (+{self.INCREMENTOS[caracteristica]})'
                         f'  atual: {valores[caracteristica]}')
                linhas_botoes.append([sg.Button(texto, size=(28, 2), key=chave, button_color=('white', 'black'),
                                                border_width=0, font=("Lucida", 12, 'bold'))])
            rodape = [sg.Cancel('Cancelar', key='0', button_color=('black', 'red'))] if permite_cancelar else []
            layout = [
                [sg.Column(
                    [[sg.Text('=== DISTRIBUIÇÃO DE PONTOS ===', font=("Lucida", 25))],
                     [sg.Text(f'Você tem {pontos_restantes} ponto(s) para distribuir', font=("Lucida", 15, 'bold'))]]
                    + linhas_botoes + [rodape],
                    element_justification='center'
                )]
            ]
            self.__window = sg.Window('=== DISTRIBUIÇÃO DE PONTOS ===', layout)
            button, values = self.__window.Read()
            self.__window.Close()

            if button in botoes:
                caracteristica = botoes[button]
                valores[caracteristica] += self.INCREMENTOS[caracteristica]
                pontos_restantes -= 1
            elif permite_cancelar:
                return None
            # Sem permissão de cancelar, fechar a janela apenas a reabre: os pontos precisam ser usados.

        return valores
