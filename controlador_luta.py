from Telas.tela_luta import TelaLuta
from random import randint


class ControladorLuta:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__tela_luta = TelaLuta()
        self.__lutas = []
        self.__start_game = False
        self.__quantidade_lutadores = 0
        self.__fase = None
        self.__boxeador_usuario = None
        self.__vitoria_boxeador_usuario = False

    @property
    def lista_lutas(self):
        return self.__lutas

    @property
    def boxeador_usuario(self):
        return self.__boxeador_usuario

    @property
    def vitoria_boxeador_usuario(self):
        return self.__vitoria_boxeador_usuario

    def iniciar_jogo(self):
        lutador_atual = None
        if self.__controlador_central.controlador_torneio.torneio_criado:
            lista_lutas = self.__controlador_central.controlador_torneio.lutas
            numero_lutadores = int(self.__controlador_central.controlador_torneio.torneio_atual.numero_lutas * 2)
            if numero_lutadores == 4:
                self.__fase = 'semi-final'
            elif numero_lutadores == 8:
                self.__fase = 'quartas-de-final'
            for luta in lista_lutas:
                if not luta.boxeador_um.boxeador_cpu:
                    jogador_usuario = luta.boxeador_um
                    jogador_adversario = luta.boxeador_dois
                elif not luta.boxeador_dois.boxeador_cpu:
                    jogador_usuario = luta.boxeador_dois
                    jogador_adversario = luta.boxeador_um
                if not luta.boxeador_um.boxeador_cpu or not luta.boxeador_dois.boxeador_cpu:
                    self.__controlador_central.controlador_torneio.mostrar_luta_usuario(jogador_usuario, jogador_adversario)
                    luta_um = self.iniciar_luta(jogador_usuario, jogador_adversario)
                    if luta_um:
                        if self.__fase == 'semi-final':
                            self.__fase = 'final'
                            luta_final = [jogador_usuario, self.__controlador_central.controlador_torneio.lutas[3]]
                        elif self.__fase == 'quartas-de-final':
                            self.__fase = 'semi-final'


        else:
            self.__tela_luta.mostrar_mensagem("------------------------------ATENÇÃO------------------------------")
            self.__tela_luta.mostrar_mensagem("Não há nenhum torneio cadastrado, é necessário cadastrar o torneio antes")
            self.__tela_luta.mostrar_mensagem("------------------------------------------------------------------")


    def iniciar_luta(self, boxeador_usuario, boxeador_adversario):
        self.__controlador_central.controlador_boxeador.verifica_jogadores_maquina()
        round = 1
        jogada = 0
        game_start = True
        while boxeador_usuario.caracteristica.vida > 0 or boxeador_adversario.caracteristica.vida > 0 or game_start or round <= 4:
            self.mostrar_luta(boxeador_usuario, boxeador_adversario)
            escolha_inicial = self.__tela_luta.tela_inicio_luta_opcoes()
            if escolha_inicial == 0:
                self.__controlador_central.inicializa_sistema()
            else:
                self.mostrar_luta(boxeador_usuario, boxeador_adversario)
            # Ataque da CPU
            habilidade_escolhida_cpu = self.escolher_habilidade_cpu()
            self.__tela_luta.mostrar_mensagem('-'*50)
            if habilidade_escolhida_cpu.tipo == 'Ataque':
                self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} usou a habilidade {habilidade_escolhida_cpu.tipo} e te dara {habilidade_escolhida_cpu.dano} de dano")
            elif habilidade_escolhida_cpu.tipo == 'Defesa':
                self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} usou a habilidade {habilidade_escolhida_cpu.tipo} e bloqueará em {habilidade_escolhida_cpu.taxa_defesa} % o dano")
            elif habilidade_escolhida_cpu.tipo == 'Esquiva':
                self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} usou a habilidade {habilidade_escolhida_cpu.tipo} e tem {habilidade_escolhida_cpu.taxa_esquiva} % de chance de esquivar do dano")
            self.__tela_luta.mostrar_mensagem('-'*50)
            # Ataque do usuário
            # Escolha da habilidade
            for habilidade in boxeador_usuario.habilidades:
                if habilidade.tipo == 'Ataque':
                    self.__tela_luta.mostrar_habilidade_ataque(habilidade)
                elif habilidade.tipo == 'Defesa':
                    self.__tela_luta.mostrar_habilidade_defesa(habilidade)
                elif habilidade.tipo == 'Esquiva':
                    self.__tela_luta.mostrar_habilidade_esquiva(habilidade)
            escolha_habilidade = self.__tela_luta.le_num_inteiro("Escolha a habilidade que deseja usar: ")
            habilidada_escolhida_usuario = self.busca_por_id(escolha_habilidade, boxeador_usuario.habilidades)

            if habilidade_escolhida_cpu.tipo == 'Ataque' and habilidada_escolhida_usuario.tipo == 'Ataque':
                # Ataque do usuário

                if habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina:
                    dano_causado_ao_usuario = boxeador_usuario.caracteristica.forca + habilidada_escolhida_usuario.dano
                    boxeador_adversario.caracteristica.vida -= dano_causado_ao_usuario
                    boxeador_usuario.caracteristica.stamina -= habilidada_escolhida_usuario.custo

                # Ataque da CPU
                if habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina:
                    dano_causado_a_cpu = boxeador_adversario.caracteristica.forca + habilidade_escolhida_cpu.dano
                    boxeador_usuario.caracteristica.vida -= dano_causado_a_cpu
                    boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

            elif ((habilidade_escolhida_cpu.tipo == 'Ataque' and habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina)
                    and habilidada_escolhida_usuario.tipo == 'Defesa' and habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina):

                # Ataque da CPU e defesa do usuário
                dano_causado_ao_usuario = boxeador_adversario.caracteristica.forca + habilidade_escolhida_cpu.dano
                taxa_defesa = habilidada_escolhida_usuario.taxa_defesa / 100
                dano_com_defesa = dano_causado_ao_usuario * taxa_defesa
                boxeador_usuario.caracteristica.vida -= dano_com_defesa
                boxeador_usuario.caracteristica.stamina -= habilidada_escolhida_usuario.custo
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

            elif ((habilidade_escolhida_cpu.tipo == 'Ataque' and habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina)
                    and habilidada_escolhida_usuario.tipo == 'Esquiva' and habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina):
                chance_desvio = habilidada_escolhida_usuario.taxa_esquiva
                # Gerar um número aleatório entre 1 e 100
                numero_aleatorio = randint(1, 100)

                # Verificar se o número aleatório está dentro da chance de desvio
                if numero_aleatorio <= chance_desvio:
                    self.__tela_luta.mostrar_mensagem("WOW que amenteigado que você está! Ataque desviado!")
                else:
                    dano_cpu = boxeador_adversario.caracteristica.forca + habilidade_escolhida_cpu.dano
                    boxeador_usuario.caracteristica.vida -= dano_cpu
                    self.__tela_luta.mostrar_mensagem(f"Hoje não campeão, você não conseguiu desviar do ataque e tomou {dano_cpu} de dano")

                boxeador_usuario.caracteristica.stamina -= habilidada_escolhida_usuario.custo
                boxeador_usuario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

            elif ((habilidada_escolhida_usuario.tipo == 'Ataque' and habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina)
                    and habilidade_escolhida_cpu.tipo == 'Defesa' and habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina):
                # Ataque do usuário e defesa da CPU
                dano_causado_a_cpu = boxeador_usuario.caracteristica.forca + habilidada_escolhida_usuario.dano
                taxa_defesa = habilidade_escolhida_cpu.taxa_defesa / 100
                dano_com_defesa = dano_causado_a_cpu * taxa_defesa
                boxeador_adversario.caracteristica.vida -= dano_com_defesa
                boxeador_usuario.caracteristica.stamina -= habilidada_escolhida_usuario.custo
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

            elif ((habilidada_escolhida_usuario.tipo == 'Ataque' and habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina)
                    and habilidade_escolhida_cpu.tipo == 'Esquiva' and habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina):
                chance_desvio = habilidade_escolhida_cpu.taxa_esquiva
                # Gerar um número aleatório entre 1 e 100
                numero_aleatorio = randint(1, 100)

                # Verificar se o número aleatório está dentro da chance de desvio
                if numero_aleatorio <= chance_desvio:
                    self.__tela_luta.mostrar_mensagem("WOW que amenteigado que você está! Ataque desviado!")
                else:
                    dano_usuario = boxeador_usuario.caracteristica.forca + habilidada_escolhida_usuario.dano
                    boxeador_adversario.caracteristica.vida -= dano_usuario
                    self.__tela_luta.mostrar_mensagem(f"Hoje não campeão, você não conseguiu desviar do ataque e tomou {dano_usuario} de dano")

                boxeador_usuario.caracteristica.stamina -= habilidada_escolhida_usuario.custo
                boxeador_adversario.caracteristica.stamina -= habilidade_escolhida_cpu.custo

            elif ((habilidada_escolhida_usuario.tipo == 'Defesa' and habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina)
                    and habilidade_escolhida_cpu.tipo == 'Esquiva' and habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina
                    or (habilidada_escolhida_usuario.tipo == 'Esquiva' and habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina
                    and habilidade_escolhida_cpu.tipo == 'Defesa' and habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina
                    or (habilidada_escolhida_usuario.tipo == 'Defesa' and habilidada_escolhida_usuario.custo < boxeador_usuario.caracteristica.stamina
                    and habilidade_escolhida_cpu.tipo == 'Defesa' and habilidade_escolhida_cpu.custo < boxeador_adversario.caracteristica.stamina))):
                self.__tela_luta.mostrar_mensagem("Você e seu adversário usaram habilidades de defesa ou esquiva, nada aconteceu")

            else:
                self.__tela_luta.mostrar_mensagem("Você não tem stamina suficiente para usar essa habilidade")
                self.__tela_luta.mostrar_mensagem("Tente novamente")
                self.iniciar_luta(boxeador_usuario, boxeador_adversario)

            jogada =+ 1
            if jogada == 3:
                jogada = 0
                round += 1

            if round == 4:
                self.__tela_luta.mostrar_mensagem("O jogo acabou")
                if boxeador_usuario.caracteristica.vida > boxeador_adversario.caracteristica.vida:
                    self.__tela_luta.mostrar_mensagem(f"O {boxeador_usuario.apelido} ganhou a luta")
                    self.mostrar_vitoria_boxeador_um(boxeador_usuario, boxeador_adversario)
                    self.__vitoria_boxeador_usuario = True
                    return self.__vitoria_boxeador_usuario
                elif boxeador_usuario.caracteristica.vida < boxeador_adversario.caracteristica.vida:
                    self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} ganhou a luta")
                    self.mostrar_vitoria_boxeador_dois(boxeador_usuario, boxeador_adversario)
                else:
                    self.__tela_luta.mostrar_mensagem("Empate")
                    cara_coroa = randint(0, 1)
                    self.__tela_luta.mostrar_mensagem("Jogo será decidido no cara ou coroa")
                    if cara_coroa == 0:
                        self.__tela_luta.mostrar_mensagem(f"O {boxeador_usuario.apelido} ganhou a luta")
                        self.mostrar_vitoria_boxeador_um(boxeador_usuario, boxeador_adversario)
                        self.__vitoria_boxeador_usuario = True
                        return self.__vitoria_boxeador_usuario
                    else:
                        self.__tela_luta.mostrar_mensagem(f"O {boxeador_adversario.apelido} ganhou a luta")
                        self.mostrar_vitoria_boxeador_dois(boxeador_usuario, boxeador_adversario)
    def escolher_habilidade_cpu(self):
        lista_habilidades = self.__controlador_central.controlador_habilidade.habilidades
        id_escolhido = randint(1, len(lista_habilidades) - 1)
        for habilidades in lista_habilidades:
            if habilidades.id == id_escolhido:
                if habilidades.tipo == 'Ataque':
                    return habilidades
                elif habilidades.tipo == 'Defesa':
                    return habilidades
                elif habilidades.tipo == 'Esquiva':
                    return habilidades
        return None, None

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
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade,
                                          boxeador_um.apelido, boxeador_dois.apelido,
                                          )

    def mostrar_vitoria_boxeador_um(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_vitoria_boxeador_um(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade,
                                          boxeador_um.apelido, boxeador_dois.apelido)

    def mostrar_vitoria_boxeador_dois(self, boxeador_um, boxeador_dois):
        self.__tela_luta.tela_luta_vitoria_boxeador_dois(boxeador_um.caracteristica.vida,
                                          boxeador_dois.caracteristica.vida,
                                          boxeador_um.caracteristica.stamina,
                                          boxeador_dois.caracteristica.stamina,
                                          boxeador_um.nacionalidade, boxeador_dois.nacionalidade,
                                          boxeador_um.apelido, boxeador_dois.apelido)
