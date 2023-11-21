from abc import ABC, abstractmethod


class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self):
        pass

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
