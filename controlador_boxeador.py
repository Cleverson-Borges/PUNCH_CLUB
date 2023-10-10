from Entidades.boxeador import Boxeador

class BoxeadorController:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__boxeadores = []
        self.__boxeador_atual = None

    @property
    def boxeadores(self):
        return self.__boxeadores

    @property
    def boxeador_atual(self):
        return self.__boxeador_atual

    @boxeador_atual.setter
    def boxeador_atual(self, boxeador:Boxeador):
        if isinstance(boxeador, Boxeador):
            self.__boxeador_atual = boxeador
        else:
            raise TypeError('O boxeador deve ser uma instância da classe Boxeador')

    def cadastrar_boxeador(self, boxeador:Boxeador):
        self.__controlador_central.controlador_status.cadastrar_status(boxeador.status)
        for habilidade in range(3):
            habilidade_escolhida = self.__controlador_central.controlador_habilidade.escolher_habilidade()
            boxeador.habilidades.append(habilidade_escolhida)
        if self.verificar_boxeador(boxeador):
            self.__boxeadores.append(boxeador)

    def listar_habilidades(self, boxeador:Boxeador):
        pass


    def verificar_boxeador(self, boxeador:Boxeador):
        if isinstance(boxeador, Boxeador):
            return True
        return None
