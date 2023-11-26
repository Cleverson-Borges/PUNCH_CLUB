from DAOs.dao import DAO
from Entidades.torneio import Torneio


class TorneioDAO(DAO):
    def __init__(self):
        super().__init__('torneios.pkl')

    def add(self, torneio: Torneio):
        if((torneio is not None) and isinstance(torneio, Torneio) and isinstance(torneio.id_torneio, int)):
            super().add(torneio.id_torneio, torneio)

    def update(self, torneio: Torneio):
        if ((torneio is not None) and isinstance(torneio, torneio) and isinstance(torneio.id_torneio, int)):
            super().update(torneio.id_torneio, torneio)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, torneio:Torneio):
        if(isinstance(torneio.id_torneio,int)):
            return super().remove(torneio.id_torneio)