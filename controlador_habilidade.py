from Entidades.habilidade import Habilidade
from Telas.tela_habilidade import TelaHabilidade
from Entidades.ataque import Ataque
from Entidades.defesa import Defesa
from Entidades.esquiva import Esquiva


class ControladorHabilidade:
    def __init__(self):
        #self.__controlador_central = controlador_central
        self.__habilidades = []
        self.__tela_habilidade = TelaHabilidade()

    @property
    def habilidades(self):
        return self.__habilidades

    def cadastrar_habilidade(self, habilidade:Habilidade):
        if isinstance(habilidade, Habilidade):
            self.__habilidades.append(habilidade)
        else:
            raise TypeError('A habilidade deve ser uma instância da classe Habilidade')

    def habilidade_atual(self, habilidade):
        if isinstance(habilidade, Habilidade):
            self.__habilidade_atual = habilidade
        else:
            raise TypeError('A habilidade deve ser uma instância da classe Habilidade')

    def base_de_habilidades(self):
        habilidade1 = Ataque(1,'Jab', 'Soco direto', 'Ataque', 3, 3)
        habilidade2 = Ataque(2, 'Hook', 'Soco gancho', 'Ataque', 3, 5)
        habilidade3 = Ataque(3, 'Uppercut', 'Soco Uppercut', 'Ataque', 5, 8)
        habilidade4 = Defesa(4, 'Bloqueio', 'Bloqueio de soco', 'Defesa', 3, 35)
        habilidade5 = Defesa(5, 'Cobertura', 'Cobrir a cabeça e o corpo com os braços', 'Defesa', 7, 75)
        habilidade6 = Defesa(6, 'Clinch', 'Segurar o oponente para interromper os ataques', 'Defesa', 9, 90)
        habilidade7 = Esquiva(7,'Esquiva rápida', 'Esquiva rápida para desviar de socos', 'Esquiva', 10, 15)
        habilidade8 = Esquiva(8, 'Esquiva diagonal', 'Esquiva diagonal para evitar ataques', 'Esquiva', 20, 25)
        habilidade9 = Esquiva(9, 'Esquiva para trás', 'Movimento de recuo para escapar de golpes', 'Esquiva', 25, 30)
        self.__habilidades.append(habilidade1)
        self.__habilidades.append(habilidade2)
        self.__habilidades.append(habilidade3)
        self.__habilidades.append(habilidade4)
        self.__habilidades.append(habilidade5)
        self.__habilidades.append(habilidade6)
        self.__habilidades.append(habilidade7)
        self.__habilidades.append(habilidade8)
        self.__habilidades.append(habilidade9)

    def adicionar_habilidade(self):
        contador = 0
        habilidades_escolhidas = []
        while contador <= 4:
            habilidade_escolhida = self.__tela_habilidade.selecionar_tipo()
            if habilidade_escolhida == 1:
                self.busca_habilidade('Ataque')
                habilidades_escolhidas.append(self.selecao_habilidade())
                contador += 1
            elif habilidade_escolhida == 2:
                self.busca_habilidade('Defesa')
                habilidades_escolhidas.append(self.selecao_habilidade())
                contador += 1
            elif habilidade_escolhida == 3:
                self.busca_habilidade('Esquiva')
                habilidades_escolhidas.append(self.selecao_habilidade())
                contador += 1
    def selecao_habilidade(self):
        id = self.__tela_habilidade.obtem_id()
        habilidade_escolhida = self.busca_por_id(id)
        if  habilidade_escolhida is not None:
            return habilidade_escolhida

    def busca_por_id(self, id):
        if id == 0:
            self.__tela_habilidade.selecionar_tipo()
        for habilidade in self.habilidades:
            if habilidade.id == id:
                return habilidade
        return None

    def busca_habilidade(self, tipo):
        # FALTAAA ADICIONAR INFORMAÇÃO ADICIONAL
        for habilidade in self.__habilidades:
            if habilidade.tipo == tipo:
                self.__tela_habilidade.mostrar_habilidade(habilidade)



