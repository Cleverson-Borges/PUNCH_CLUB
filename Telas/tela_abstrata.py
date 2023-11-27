from abc import ABC, abstractmethod
import PySimpleGUI as sg


class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def print_mensagem(self, mensagem):
        sg.popup('', mensagem)

    def le_num_inteiro(self, valor_lido, ints_validos=None):
        while True:
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
            try:
                valor_float = float(valor_lido)
                if (min_valor is not None and valor_float < min_valor) or (
                        max_valor is not None and valor_float > max_valor):
                    raise ValueError
                return valor_float
            except ValueError:
                sg.popup(f"O valor deve estar entre {min_valor} e {max_valor}.")
                valor_lido = sg.popup_get_text('Digite um valor válido:')

    def le_str_valida(self, valor_lido):
        while True:
            try:
                if not isinstance(valor_lido, str) or len(valor_lido) != 3 or not valor_lido.isalpha():
                    raise ValueError
                return valor_lido.upper()
            except ValueError:
                sg.popup('Entrada Inválida! Digite exatamente 3 letras.')
                valor_lido = sg.popup_get_text('Digite uma entrada de 3 letras:')
