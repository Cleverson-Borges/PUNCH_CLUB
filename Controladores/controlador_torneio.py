from Telas.tela_torneio import TelaTorneio
from Entidades.luta import Luta
from Entidades.torneio import Torneio
from DAOs.torneio_dao import TorneioDAO
import random
from enum import Enum


class TorneioNumbers(Enum):
    ID_INICIAL_TORNEIO = 1


class ControladorTorneio:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__tela_torneio = TelaTorneio()
        self.__torneio_dao = TorneioDAO()

    @property
    def torneios(self):
        return self.__torneio_dao.get_all()

    def cadastrar_torneio(self):
        controlador_boxeador = self.__controlador_central.controlador_boxeador
        if not controlador_boxeador.verifica_jogadores_maquina():
            return

        dados_torneio = self.__tela_torneio.cadastrar_torneio(Torneio.NUMEROS_LUTADORES_VALIDOS)
        if dados_torneio is None:
            return
        numero_lutadores = dados_torneio['numero_lutadores']
        boxeadores_cpu = controlador_boxeador.retornar_boxeadores_cpu()
        if numero_lutadores - 1 > len(boxeadores_cpu):
            self.__tela_torneio.mostrar_mensagem(f"Não há boxeadores da CPU suficientes para um torneio "
                                                 f"de {numero_lutadores} lutadores.")
            return

        jogador_usuario = self.seleciona_jogador_usuario()
        if jogador_usuario is None:
            return

        id_torneio = self.cadastra_id_torneio(TorneioNumbers.ID_INICIAL_TORNEIO.value)
        torneio_cadastrado = Torneio(dados_torneio['nome_torneio'], id_torneio, jogador_usuario.cpf, numero_lutadores)
        self.criar_lutas_torneio(torneio_cadastrado, jogador_usuario, boxeadores_cpu)
        self.__torneio_dao.add(torneio_cadastrado)
        self.__tela_torneio.mostrar_mensagem(f"Torneio {torneio_cadastrado.nome_torneio} cadastrado com o ID "
                                             f"{torneio_cadastrado.id_torneio}!")
        self.mostrar_torneio(torneio_cadastrado)

    def seleciona_jogador_usuario(self):
        controlador_boxeador = self.__controlador_central.controlador_boxeador
        controlador_boxeador.listar_boxeadores_edicao_exclusao()
        cpf_jogador_usuario = self.__tela_torneio.obtem_cpf()
        if cpf_jogador_usuario is None:
            return None
        jogador_usuario = controlador_boxeador.busca_por_cpf(cpf_jogador_usuario)
        if jogador_usuario is None or jogador_usuario.boxeador_cpu:
            self.__tela_torneio.mostrar_mensagem("Esse CPF não pertence a um boxeador seu!")
            return None
        if self.verifica_se_cpf_ja_cadastrado(cpf_jogador_usuario):
            return None
        return jogador_usuario

    def busca_torneio_por_id(self, id_torneio):
        return self.__torneio_dao.get(id_torneio)

    def retorna_lista_ids_cadastrados_torneios(self):
        return [torneio.id_torneio for torneio in self.__torneio_dao.get_all()]

    def cadastra_id_torneio(self, id_torneio):
        lista_ids_existentes = self.retorna_lista_ids_cadastrados_torneios()
        while id_torneio in lista_ids_existentes:
            id_torneio += 1
        return id_torneio

    def criar_lutas_torneio(self, torneio, jogador_usuario, boxeadores_cpu):
        # Sorteia os adversários e monta a primeira fase do chaveamento.
        adversarios = random.sample(boxeadores_cpu, torneio.numero_lutadores - 1)
        cpfs_participantes = [jogador_usuario.cpf] + [boxeador.cpf for boxeador in adversarios]
        random.shuffle(cpfs_participantes)
        torneio.adicionar_fase(self.montar_lutas(cpfs_participantes))

    def montar_lutas(self, cpfs):
        return [Luta(cpfs[i], cpfs[i + 1]) for i in range(0, len(cpfs), 2)]

    def avancar_fase(self, torneio):
        # Chamado quando todas as lutas da fase atual terminaram.
        vencedores = torneio.vencedores_fase_atual()
        if len(vencedores) == 1:
            torneio.cpf_campeao = vencedores[0]
        else:
            torneio.adicionar_fase(self.montar_lutas(vencedores))
        self.salvar_torneio(torneio)

    def salvar_torneio(self, torneio):
        self.__torneio_dao.update(torneio)

    def nome_boxeador(self, cpf):
        boxeador = self.__controlador_central.controlador_boxeador.busca_por_cpf(cpf)
        return boxeador.nome if boxeador is not None else f'(CPF {cpf} removido)'

    def mostrar_torneio(self, torneio):
        fases = []
        for fase in torneio.fases:
            fases.append({'nome': Torneio.nome_da_fase(len(fase)),
                          'lutas': [{'boxeador_um': self.nome_boxeador(luta.cpf_boxeador_um),
                                     'boxeador_dois': self.nome_boxeador(luta.cpf_boxeador_dois),
                                     'vencedor': self.nome_boxeador(luta.cpf_vencedor) if luta.finalizada else None}
                                    for luta in fase]})
        self.__tela_torneio.mostrar_chaveamento(torneio.nome_torneio, fases)

    def mostrar_luta_usuario(self, boxeador_um, boxeador_dois, torneio):
        nome_fase = Torneio.nome_da_fase(len(torneio.fase_atual))
        self.__tela_torneio.mostrar_luta_usuario(torneio.nome_torneio, nome_fase, boxeador_um, boxeador_dois)

    def abre_tela(self):
        escolha_tela = {1: self.cadastrar_torneio,
                        2: self.listar_e_mostrar_torneio}

        while True:
            opcao = self.__tela_torneio.tela_opcoes()
            if opcao == 0:
                return
            escolha_tela[opcao]()

    def listar_e_mostrar_torneio(self):
        if self.listar_torneios():
            id_torneio = self.__tela_torneio.obtem_id_chaveamento(self.retorna_lista_ids_validos())
            if id_torneio is not None:
                self.mostrar_torneio(self.busca_torneio_por_id(id_torneio))

    def verifica_se_cpf_ja_cadastrado(self, cpf):
        for torneio in self.__torneio_dao.get_all():
            if torneio.cpf_usuario == cpf:
                self.__tela_torneio.mostrar_mensagem("CPF já cadastrado em outro torneio!\n"
                                                     "Você não pode participar de dois torneios ao mesmo tempo!\n"
                                                     "Termine seu torneio antes!")
                return True
        return False

    def remover_torneio_por_usuario(self, usuario):
        for torneio in self.__torneio_dao.get_all():
            if torneio.cpf_usuario == usuario.cpf:
                self.__torneio_dao.remove(torneio)
                return True
        return False

    def remover_torneio(self, id_torneio):
        torneio = self.busca_torneio_por_id(id_torneio)
        if torneio is not None:
            self.__torneio_dao.remove(torneio)
        else:
            self.__tela_torneio.mostrar_mensagem("Torneio não encontrado!")

    def listar_torneios(self):
        # Retorna True se havia torneios para listar.
        if len(self.__torneio_dao.get_all()) > 0:
            lista_torneios = []
            for torneio in self.__torneio_dao.get_all():
                lista_torneios.append({"nome_torneio": torneio.nome_torneio,
                                       "id": torneio.id_torneio,
                                       "nome": self.nome_boxeador(torneio.cpf_usuario),
                                       "numero_lutadores": torneio.numero_lutadores,
                                       "fase": Torneio.nome_da_fase(len(torneio.fase_atual))})

            self.__tela_torneio.listar_torneios(lista_torneios)
            return True
        self.__tela_torneio.mostrar_mensagem("Não há torneios cadastrados!")
        return False

    def retorna_lista_ids_validos(self):
        return self.retorna_lista_ids_cadastrados_torneios()
