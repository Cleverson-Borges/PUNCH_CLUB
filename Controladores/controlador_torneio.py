from Telas.tela_torneio import TelaTorneio
from Entidades.luta import Luta
from Entidades.torneio import Torneio
from DAOs.torneio_dao import TorneioDAO
import random
from enum import Enum


class TorneioNumbers(Enum):
    SEMI_FINAL_NUMERO_DE_LUTAS = 2
    QUARTAS_DE_FINAL_NUMERO_DE_LUTAS = 4
    MULTIPLICADOR_LUTADORES = 2
    ID_INICIAL_TORNEIO = 1


class ControladorTorneio:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__tela_torneio = TelaTorneio()
        self.__torneio_dao = TorneioDAO()
        self.__jogador_usuario = None

    @property
    def torneios(self):
        return self.__torneio_dao.get_all()

    @property
    def jogador_usuario(self):
        return self.__jogador_usuario

    @jogador_usuario.setter
    def jogador_usuario(self, jogador):
        self.__jogador_usuario = jogador

    def cadastrar_torneio(self):
        self.__controlador_central.controlador_boxeador.verifica_jogadores_maquina()
        fase_atual = TorneioNumbers.SEMI_FINAL_NUMERO_DE_LUTAS.value
        dados_torneio = self.__tela_torneio.cadastrar_torneio()
        nome_torneio = dados_torneio["nome_torneio"]
        numero_lutadores = dados_torneio["numero_lutadores"]
        numero_lutas = int(numero_lutadores / TorneioNumbers.MULTIPLICADOR_LUTADORES.value)
        if numero_lutas == TorneioNumbers.SEMI_FINAL_NUMERO_DE_LUTAS.value:
            fase_atual = 'semi-final'
        elif numero_lutas == TorneioNumbers.QUARTAS_DE_FINAL_NUMERO_DE_LUTAS.value:
            fase_atual = 'quartas-de-final'
        id_torneio = self.cadastra_id_torneio(TorneioNumbers.ID_INICIAL_TORNEIO.value)
        torneio_cadastrado = Torneio(nome_torneio, numero_lutas, fase_atual, id_torneio)
        self.criar_lutas_torneio(numero_lutadores, torneio_cadastrado)
        self.__torneio_dao.add(torneio_cadastrado)
        self.mostrar_torneio(torneio_cadastrado)

    def busca_torneio_por_id(self, id_torneio):
        for torneio in self.__torneio_dao.get_all():
            if torneio.id_torneio == id_torneio:
                return torneio
        return None

    def retorna_lista_ids_cadastrados_torneios(self):
        ids_cadastrados = []
        for torneio in self.__torneio_dao.get_all():
            ids_cadastrados.append(torneio.id_torneio)
        return ids_cadastrados

    def cadastra_id_torneio(self, id_torneio):
        lista_ids_existentes = self.retorna_lista_ids_cadastrados_torneios()
        while id_torneio in lista_ids_existentes:
            id_torneio += 1
        return id_torneio

    def criar_lutas_torneio(self, numero_lutadores, torneio):
        self.__controlador_central.controlador_boxeador.listar_boxeadores_edicao_exclusao()
        cpf_jogador_usuario = self.__tela_torneio.obtem_cpf()
        self.verifica_se_cpf_ja_cadastrado(cpf_jogador_usuario)
        jogador_usuario = self.__controlador_central.controlador_boxeador.busca_por_cpf(cpf_jogador_usuario)
        self.__jogador_usuario = jogador_usuario
        lista_jogadores = self.__controlador_central.controlador_boxeador.retornar_boxeadores_cpu()
        lista_jogadores.insert(0, jogador_usuario)
        lista_boxeadores = lista_jogadores[:(numero_lutadores)]
        contador = 0
        while contador < (len(lista_boxeadores) - 1):
            boxeador_um = lista_boxeadores[contador]
            boxeador_dois = lista_boxeadores[contador + 1]
            contador = contador + 2
            if boxeador_um.boxeador_cpu == False:
                torneio.boxeador_usuario = boxeador_um
            if boxeador_dois.boxeador_cpu == False:
                torneio.boxeador_usuario = boxeador_dois
            torneio.adicionar_luta(Luta(boxeador_um, boxeador_dois))

    def mostrar_torneio(self, torneio):
        self.__tela_torneio.mostrar_torneio(torneio.nome_torneio, int(torneio.numero_lutas * 2), torneio.id_torneio)
        for luta in torneio.lista_lutas:
                self.__tela_torneio.mostrar_chaveamento(torneio.nome_torneio, luta.boxeador_um, luta.boxeador_dois, torneio.numero_lutas)

    def mostrar_luta_usuario(self, boxeador_um, boxeador_dois, torneio):
        self.__tela_torneio.mostrar_luta_usuario(torneio.nome_torneio,boxeador_um, boxeador_dois)

    def gerar_lutas(self):
        lista_boxeadores = self.__controlador_central.controlador_boxeador.boxeadores
        for boxeador in range(lista_boxeadores):
            boxeador1, boxeador2 = random.sample(lista_boxeadores, 2)
            return boxeador1, boxeador2

    def mostrar_chaveamento(self, torneio):
        for luta in torneio.lutas:
            self.__tela_torneio.mostrar_chaveamento(torneio.nome_torneio, luta.boxeador_um,
                                                    luta.boxeador_dois, torneio.fase)

    def encerra_sistema(self):
        self.__controlador_central.abre_tela()

    def get_id_torneio(self, id_torneio):
        lista_ids_torneios = [torneio.id_torneio for torneio in self.__torneio_dao.get_all()]
        if id_torneio in lista_ids_torneios:
            id_torneio += 1
        return id_torneio

    def abre_tela(self):
        escolha_tela = {1: self.cadastrar_torneio,
                        0: self.encerra_sistema}

        continua = True
        while continua:
            escolha_tela[self.__tela_torneio.tela_opcoes()]()

    def verifica_se_cpf_ja_cadastrado(self, cpf):
        cpf_ja_cadastrado = False
        for torneio in self.__torneio_dao.get_all():
            if torneio.boxeador_usuario.cpf == cpf:
                cpf_ja_cadastrado = True
        if cpf_ja_cadastrado:
            self.__tela_torneio.mostrar_mensagem("CPF já cadastrado em outro torneio!")
            self.__tela_torneio.mostrar_mensagem("Você não pode participar de dois torneios ao mesmo tempo!")
            self.__tela_torneio.mostrar_mensagem("Termine seu torneio antes!")
            self.__controlador_central.abre_tela()

    def listar_torneios(self):
        if len(self.__torneio_dao.get_all()) > 0:
            for torneio in self.__torneio_dao.get_all():
                self.__tela_torneio.mostrar_torneio(torneio.nome_torneio, torneio.numero_lutas, torneio.id_torneio)
        else:
            self.__tela_torneio.mostrar_mensagem("Não há torneios cadastrados!")

    def retorna_lista_ids_validos(self):
        lista_ids_validos = []
        for torneio in self.__torneio_dao.get_all():
            lista_ids_validos.append(torneio.id_torneio)
        return lista_ids_validos
