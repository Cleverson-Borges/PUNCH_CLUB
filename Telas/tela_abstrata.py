from abc import ABC, abstractmethod
import FreeSimpleGUI as sg


class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def print_mensagem(self, mensagem):
        sg.popup('', mensagem)

    # Os leitores abaixo repetem a pergunta até receber um valor válido.
    # Se o usuário cancelar a janela de correção, retornam None.
    def le_num_inteiro(self, valor_lido, ints_validos=None):
        while True:
            if valor_lido is None:
                return None
            try:
                valor_int = int(valor_lido)
                if ints_validos is not None and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                sg.popup('Valor Inválido! Tente novamente.')
                valor_lido = sg.popup_get_text('Digite um número inteiro:')

    def le_num_inteiro_entre(self, valor_lido, min_valor=None, max_valor=None):
        while True:
            if valor_lido is None:
                return None
            try:
                valor_int = int(valor_lido)
                if (min_valor is not None and valor_int < min_valor) or (
                        max_valor is not None and valor_int > max_valor):
                    raise ValueError
                return valor_int
            except ValueError:
                sg.popup(f'O valor deve ser no minímo {min_valor} e no maximo {max_valor} ')
                valor_lido = sg.popup_get_text('Digite um valor válido: ')

    def le_num_float_entre(self, valor_lido, min_valor=None, max_valor=None):
        while True:
            if valor_lido is None:
                return None
            try:
                valor_float = float(str(valor_lido).replace(',', '.'))
                if (min_valor is not None and valor_float < min_valor) or (
                        max_valor is not None and valor_float > max_valor):
                    raise ValueError
                return valor_float
            except ValueError:
                sg.popup(f"O valor deve estar entre {min_valor} e {max_valor}.")
                valor_lido = sg.popup_get_text('Digite um valor válido:')

    def le_str_valida(self, valor_lido):
        while True:
            if valor_lido is None:
                return None
            if isinstance(valor_lido, str) and len(valor_lido) == 3 and valor_lido.isalpha():
                return valor_lido.upper()
            sg.popup('Entrada Inválida! Digite exatamente 3 letras.')
            valor_lido = sg.popup_get_text('Digite uma entrada de 3 letras:')

    def le_str_nao_vazia(self, valor_lido, nome_campo):
        while True:
            if valor_lido is None:
                return None
            if valor_lido.strip() != '':
                return valor_lido.strip()
            sg.popup(f'O campo {nome_campo} não pode ficar vazio.')
            valor_lido = sg.popup_get_text(f'Digite o {nome_campo}:')

    def confirmar(self, mensagem):
        return sg.popup_yes_no(mensagem, title='Confirmação') == 'Yes'
