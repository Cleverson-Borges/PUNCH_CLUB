from Telas.tela_luta import TelaLuta

class ControladorLuta:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__tela_luta = TelaLuta()
        self.__lutas = []
        self.__start_game = False
        self.__quantidade_lutadores = 0
        self.__jogador_usuario = None
        self.__fase = None

    @property
    def lista_lutas(self):
        return self.__lutas

    def iniciar_jogo(self):
        if self.__controlador_central.controlador_torneio.torneio_criado:
            lista_lutas = self.__controlador_central.controlador_torneio.lutas_torneio
            numero_lutadores = self.__controlador_central.controlador_torneio.torneio_atual.numero_lutadores
            if numero_lutadores == 4:
                self.__fase = 'semi-final'
            elif numero_lutadores == 8:
                self.__fase = 'quartas-de-final'
            for luta in lista_lutas:
                if not luta.boxeador_um.boxeador_cpu:
                    self.__jogador_usuario = luta.boxeador_um
                elif not luta.boxeador_dois.boxeador_cpu:
                    self.__jogador_usuario = luta.boxeador_dois
                if not luta.boxeador_um.boxeador_cpu or not luta.boxeador_dois.boxeador_cpu:
                    self.__controlador_central.controlador_torneio.mostrar_luta_usuario()
                    self.__controlador_central.controlador_torneio.mostrar_chaveamento(luta.boxeador_um, luta.boxeador_dois)
                    self.iniciar_luta(luta.boxeador_um, luta.boxeador_dois)

    def iniciar_luta(self, boxeador_um, boxeador_dois):
        self.__controlador_central.controlador_boxeador.verifica_jogadores_maquina()
        if not self.__jogador_usuario:
            round = 1
            jogada = 0
            game_start = True
            while boxeador_dois.vida > 0 or boxeador_um.vida > 0 or game_start or round <= 3:
                self.mostrar_luta(boxeador_um, boxeador_dois)
                escolha_inicial = self.__tela_luta.tela_inicio_luta_opcoes()
                if escolha_inicial == 0:
                    self.__controlador_central.inicializa_sistema()
                else:
                    self.mostrar_luta(boxeador_um, boxeador_dois)
                for habilidade in self.__jogador_usuario.habilidades:
                    if habilidade.tipo == 'Ataque':
                        self.__tela_luta.mostrar_habilidade_ataque(habilidade)
                    elif habilidade.tipo == 'Defesa':
                        self.__tela_luta.mostrar_habilidade_defesa(habilidade)
                    elif habilidade.tipo == 'Esquiva':
                        self.__tela_luta.mostrar_habilidade_esquiva(habilidade)
                escolha_habilidade = self.__tela_luta.le_num_inteiro("Escolha a habilidade que deseja usar: ")
                habilidada_escolhida = self.busca_por_id(escolha_habilidade, self.__jogador_usuario.habilidades)
                if habilidada_escolhida is not None:
                    if habilidada_escolhida.tipo == 'Ataque':
                        boxeador_dois.vida -= habilidada_escolhida.dano
                    elif habilidada_escolhida.tipo == 'Defesa':
                        boxeador_um.vida += habilidada_escolhida.taxa_defesa
                    elif habilidada_escolhida.tipo == 'Esquiva':
                        boxeador_um.vida += habilidada_escolhida.taxa_esquiva
                jogada =+ 1
                if jogada == 3:
                    jogada = 0
                    round += 1
        else:
            self.__tela_luta.mostra_mensagem("Você não pode lutar, pois todos os lutadores são CPU!")

    def busca_por_id(self, id, lista_habilidades):
        for habilidade in lista_habilidades:
            if habilidade.id == id:
                return habilidade
        return None

    def mostrar_luta(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_padrao(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.apelido, boxeador_dois.apelido,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade)

    def mostrar_vitoria_boxeador_um(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_vitoria_boxeador_um(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.apelido, boxeador_dois.apelido,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade)

    def mostrar_vitoria_boxeador_dois(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_vitoria_boxeador_dois(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.apelido, boxeador_dois.apelido,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade)
    def lutar(self):
        for lutas in self.__lutas:
            pass