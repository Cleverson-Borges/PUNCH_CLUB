from DAOs.dao import DAO
from Entidades.boxeador import Boxeador


class BoxeadorDAO(DAO):
    def __init__(self):
        super().__init__('boxeadores.pkl')

    def add(self, boxeador: Boxeador):
        if((boxeador is not None) and isinstance(boxeador, Boxeador) and isinstance(boxeador.cpf, int)):
            super().add(boxeador.cpf, boxeador)

    def update(self, boxeador: Boxeador):
        if ((boxeador is not None) and isinstance(boxeador, Boxeador) and isinstance(boxeador.cpf, int)):
            super().update(boxeador.cpf, boxeador)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, boxeador:Boxeador):
        if(isinstance(boxeador.cpf,int)):
            return super().remove(boxeador.cpf)