from Controladores.controlador_torneio import ControladorTorneio

class TelaTorneio:
    def __init__(self):
        self.__controlador = ControladorTorneio
        pass

    def cadastro_torneio(self):
        print("-"*5, "CADASTRAMENTO DE TORNEIO", "-"*5)
        print()
        nome_torneio = input(str("Informe o nome que deseja dar a ésta disputa: "))
        numero_lutadores = input(int("Informe quantos lutadores irão compor o torneio"
                                     "4 ou 8 já contando com você: "))
        self.__controlador.verifica_entrada_lutadores(numero_lutadores)
        return nome_torneio, numero_lutadores

    def mostrar_chveamento(self, nome_torneio, boxeador):
        print("-"*5, f"CONFIRA O CHAVEAMENTO DO TORENIO {nome_torneio}")
        print()
        print(f"CHAVE 1 = {boxeador.nome}", "vs", f"{boxeador.nome}")