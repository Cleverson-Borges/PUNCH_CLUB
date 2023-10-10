from controlador_boxeador import BoxeadorController
from controlador_habilidade import HabilityController
from controlador_status import StatusController


class CentralController:
    def __init__(self):
        self.__controlador_boxeador = BoxeadorController()
        self.__controlador_habilidade = HabilityController()
        self.__controlador_status = StatusController()


    @property
    def controlador_boxeador(self):
        return self.__controlador_boxeador

    @property
    def controlador_habilidade(self):
        return self.__controlador_habilidade

    @property
    def controlador_status(self):
        return self.__controlador_status