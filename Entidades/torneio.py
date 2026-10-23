from Entidades.luta import Luta


class Torneio():
    NUMEROS_LUTADORES_VALIDOS = (2, 4, 8, 16)

    def __init__(self, nome_torneio, id_torneio, cpf_usuario, numero_lutadores):
        if numero_lutadores not in Torneio.NUMEROS_LUTADORES_VALIDOS:
            raise ValueError('O número de lutadores deve ser 2, 4, 8 ou 16')
        self.__nome_torneio = nome_torneio
        self.__id_torneio = id_torneio
        self.__cpf_usuario = cpf_usuario
        self.__numero_lutadores = numero_lutadores
        self.__fases = []  # cada fase é uma lista de lutas
        self.__cpf_campeao = None

    @property
    def nome_torneio(self):
        return self.__nome_torneio

    @property
    def id_torneio(self):
        return self.__id_torneio

    @property
    def cpf_usuario(self):
        return self.__cpf_usuario

    @property
    def numero_lutadores(self):
        return self.__numero_lutadores

    @property
    def fases(self):
        return self.__fases

    @property
    def fase_atual(self):
        if len(self.__fases) == 0:
            return []
        return self.__fases[-1]

    @property
    def lista_lutas(self):
        return [luta for fase in self.__fases for luta in fase]

    @property
    def cpf_campeao(self):
        return self.__cpf_campeao

    @property
    def finalizado(self):
        return self.__cpf_campeao is not None

    @nome_torneio.setter
    def nome_torneio(self, nome):
        if isinstance(nome, str):
            self.__nome_torneio = nome

    @id_torneio.setter
    def id_torneio(self, id):
        if isinstance(id, int):
            self.__id_torneio = id

    @cpf_usuario.setter
    def cpf_usuario(self, cpf):
        if isinstance(cpf, int):
            self.__cpf_usuario = cpf

    @cpf_campeao.setter
    def cpf_campeao(self, cpf):
        if isinstance(cpf, int):
            self.__cpf_campeao = cpf

    def adicionar_fase(self, lutas):
        if all(isinstance(luta, Luta) for luta in lutas):
            self.__fases.append(lutas)

    def fase_atual_concluida(self):
        return all(luta.finalizada for luta in self.fase_atual)

    def vencedores_fase_atual(self):
        return [luta.cpf_vencedor for luta in self.fase_atual]

    def usuario_eliminado(self):
        for luta in self.lista_lutas:
            if luta.finalizada and luta.envolve(self.__cpf_usuario) and luta.cpf_vencedor != self.__cpf_usuario:
                return True
        return False

    @staticmethod
    def nome_da_fase(numero_lutas):
        nomes = {1: 'Final', 2: 'Semifinal', 4: 'Quartas de final', 8: 'Oitavas de final'}
        return nomes.get(numero_lutas, f'Fase de {numero_lutas} lutas')
