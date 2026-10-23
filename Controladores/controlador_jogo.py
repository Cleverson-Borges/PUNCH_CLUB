from Telas.tela_jogo import TelaJogo
from Entidades.torneio import Torneio
from random import randint, choice
from enum import Enum


class FightNumbers(Enum):
    ROUNDS = 3
    JOGADAS_POR_ROUND = 3
    RECUPERACAO_STAMINA = 4      # stamina recuperada por todos ao fim de cada jogada
    RECUPERACAO_DEFESA = 5       # stamina extra ao defender com stamina baixa
    TAXA_MAXIMA = 95             # teto (%) para chance de esquiva e redução de dano


class EstadoLutador:
    # Vida e stamina durante a luta. Fica separado do Boxeador para que a luta
    # não altere as características salvas do personagem.
    def __init__(self, boxeador, caracteristicas):
        self.boxeador = boxeador
        self.apelido = boxeador.apelido
        self.forca = caracteristicas['forca']
        self.esquiva = caracteristicas['esquiva']
        self.defesa = caracteristicas['defesa']
        self.vida_max = caracteristicas['vida']
        self.vida = caracteristicas['vida']
        self.stamina_max = caracteristicas['stamina']
        self.stamina = caracteristicas['stamina']

    def pode_usar(self, habilidade):
        return habilidade.custo <= self.stamina


class ControladorJogo:
    def __init__(self, controlador_central):
        self.__controlador_central = controlador_central
        self.__tela_jogo = TelaJogo()

    def escolher_torneio(self):
        controlador_torneio = self.__controlador_central.controlador_torneio
        controlador_torneio.listar_torneios()
        lista_ids_validos = controlador_torneio.retorna_lista_ids_validos()
        id_torneio = self.__tela_jogo.obtem_id_torneio(lista_ids_validos)
        if id_torneio is None:
            return None
        return controlador_torneio.busca_torneio_por_id(id_torneio)

    def iniciar_jogo(self):
        if not self.__controlador_central.controlador_boxeador.verifica_jogadores_maquina():
            return
        if len(self.__controlador_central.controlador_torneio.torneios) == 0:
            self.__tela_jogo.mostrar_mensagem("Não há nenhum torneio cadastrado, cadastre antes")
            return
        torneio = self.escolher_torneio()
        if torneio is not None:
            self.jogar_torneio(torneio)

    def jogar_torneio(self, torneio):
        controlador_torneio = self.__controlador_central.controlador_torneio
        controlador_boxeador = self.__controlador_central.controlador_boxeador
        usuario = controlador_boxeador.busca_por_cpf(torneio.cpf_usuario)
        if usuario is None:
            self.__tela_jogo.mostrar_mensagem("O boxeador deste torneio não existe mais!")
            controlador_torneio.remover_torneio(torneio.id_torneio)
            return

        controlador_torneio.mostrar_torneio(torneio)
        while True:
            # As lutas entre boxeadores da CPU da fase atual são simuladas automaticamente.
            luta_usuario = None
            for luta in torneio.fase_atual:
                if luta.finalizada:
                    continue
                if luta.envolve(usuario.cpf):
                    luta_usuario = luta
                    continue
                boxeador_um = controlador_boxeador.busca_por_cpf(luta.cpf_boxeador_um)
                boxeador_dois = controlador_boxeador.busca_por_cpf(luta.cpf_boxeador_dois)
                luta.cpf_vencedor = self.simular_luta(boxeador_um, boxeador_dois).cpf
            controlador_torneio.salvar_torneio(torneio)

            if luta_usuario is not None:
                cpf_adversario = (luta_usuario.cpf_boxeador_dois if luta_usuario.cpf_boxeador_um == usuario.cpf
                                  else luta_usuario.cpf_boxeador_um)
                adversario = controlador_boxeador.busca_por_cpf(cpf_adversario)
                controlador_torneio.mostrar_luta_usuario(boxeador_um=usuario, boxeador_dois=adversario, torneio=torneio)
                nome_fase = Torneio.nome_da_fase(len(torneio.fase_atual))
                resultado = self.iniciar_luta(usuario, adversario, nome_fase)
                self.retorna_informacoes_lista(resultado['jogadas_usuario'], resultado['dano_causado_usuario'])

                if not resultado['vitoria_jogador_usuario']:
                    luta_usuario.cpf_vencedor = adversario.cpf
                    self.__tela_jogo.mostrar_mensagem("------ GAME OVER ------\nVocê foi eliminado do torneio.")
                    controlador_torneio.remover_torneio(torneio.id_torneio)
                    return
                luta_usuario.cpf_vencedor = usuario.cpf
                controlador_boxeador.distribuir_pontos_vitoria(usuario)

            controlador_torneio.avancar_fase(torneio)
            if torneio.finalizado:
                self.__tela_jogo.mostrar_campeao(boxeador_campeao=usuario, nome_torneio=torneio.nome_torneio)
                controlador_torneio.mostrar_torneio(torneio)
                controlador_torneio.remover_torneio(torneio.id_torneio)
                return

            controlador_torneio.mostrar_torneio(torneio)
            proxima_fase = Torneio.nome_da_fase(len(torneio.fase_atual))
            if not self.__tela_jogo.confirmar(f"Próxima luta: {proxima_fase}.\nDeseja lutar agora?"):
                self.__tela_jogo.mostrar_mensagem("Progresso salvo! Continue o torneio pelo START GAME.")
                return

    def iniciar_luta(self, boxeador_usuario, boxeador_adversario, nome_fase=''):
        controlador_boxeador = self.__controlador_central.controlador_boxeador
        usuario = EstadoLutador(boxeador_usuario, controlador_boxeador.caracteristicas_de_luta(boxeador_usuario))
        cpu = EstadoLutador(boxeador_adversario, controlador_boxeador.caracteristicas_de_luta(boxeador_adversario))
        jogadas_usuario = []
        dano_causado_usuario = 0

        for numero_round in range(1, FightNumbers.ROUNDS.value + 1):
            if usuario.vida <= 0 or cpu.vida <= 0:
                break
            if not self.mostrar_luta(usuario, cpu, numero_round, nome_fase):
                return self.desistencia(jogadas_usuario, dano_causado_usuario)

            for jogada in range(FightNumbers.JOGADAS_POR_ROUND.value):
                habilidade_cpu = self.escolher_habilidade_cpu(cpu)
                if habilidade_cpu is None:
                    mensagem = f"O {cpu.apelido} está sem stamina e vai descansar"
                else:
                    mensagem = f"O {cpu.apelido} vai usar {habilidade_cpu.nome} ({habilidade_cpu.tipo})"

                escolha_habilidade = self.mostrar_e_escolher_habilidade(usuario, cpu, mensagem,
                                                                        boxeador_usuario.habilidades)
                if escolha_habilidade is False:
                    return self.desistencia(jogadas_usuario, dano_causado_usuario)
                habilidade_usuario = None
                if escolha_habilidade != 'DESCANSAR':
                    habilidade_usuario = self.busca_por_id(escolha_habilidade, boxeador_usuario.habilidades)
                    jogadas_usuario.append(habilidade_usuario)

                relatorio, dano = self.resolver_turno(usuario, habilidade_usuario, cpu, habilidade_cpu)
                dano_causado_usuario += dano
                self.__tela_jogo.mostrar_mensagem('\n'.join(relatorio))
                if usuario.vida <= 0 or cpu.vida <= 0:
                    break

        vitoria_jogador_usuario = self.decidir_vencedor(usuario, cpu, mostrar=True) is usuario
        return {'vitoria_jogador_usuario': vitoria_jogador_usuario,
                'jogadas_usuario': jogadas_usuario,
                'dano_causado_usuario': round_dano(dano_causado_usuario)}

    def desistencia(self, jogadas_usuario, dano_causado_usuario):
        self.__tela_jogo.mostrar_mensagem("Você jogou a toalha! Desistir conta como derrota.")
        return {'vitoria_jogador_usuario': False,
                'jogadas_usuario': jogadas_usuario,
                'dano_causado_usuario': round_dano(dano_causado_usuario)}

    def decidir_vencedor(self, lutador_um, lutador_dois, mostrar=False):
        mensagens = ["O jogo acabou"]
        if lutador_um.vida > lutador_dois.vida:
            vencedor = lutador_um
        elif lutador_um.vida < lutador_dois.vida:
            vencedor = lutador_dois
        else:
            mensagens.append("Empate! O jogo será decidido no cara ou coroa")
            vencedor = lutador_um if randint(0, 1) == 0 else lutador_dois
        mensagens.append(f"O {vencedor.apelido} ganhou a luta")
        if mostrar:
            self.__tela_jogo.mostrar_mensagem('\n'.join(mensagens))
        return vencedor

    def resolver_turno(self, usuario, habilidade_usuario, cpu, habilidade_cpu):
        # Os dois lutadores agem ao mesmo tempo. Retorna (linhas do relatório, dano causado pelo usuário).
        relatorio = []
        acao_usuario = self.pagar_habilidade(usuario, habilidade_usuario, relatorio)
        acao_cpu = self.pagar_habilidade(cpu, habilidade_cpu, relatorio)
        habilidade_cpu = acao_cpu

        dano_usuario = self.calcular_dano(usuario, acao_usuario, cpu, habilidade_cpu, relatorio)
        dano_cpu = self.calcular_dano(cpu, habilidade_cpu, usuario, acao_usuario, relatorio)
        cpu.vida = round_dano(cpu.vida - dano_usuario)
        usuario.vida = round_dano(usuario.vida - dano_cpu)

        if dano_usuario == 0 and dano_cpu == 0 and not relatorio:
            relatorio.append("Nenhum golpe acertou o alvo nesta jogada")

        for lutador, habilidade in ((usuario, acao_usuario), (cpu, habilidade_cpu)):
            # Defender com stamina baixa ajuda a recuperar o fôlego (regra da documentação)
            if (habilidade is not None and habilidade.tipo == 'Defesa'
                    and lutador.stamina < lutador.stamina_max / 2):
                lutador.stamina += FightNumbers.RECUPERACAO_DEFESA.value
                relatorio.append(f"O {lutador.apelido} se defendeu e recuperou o fôlego "
                                 f"(+{FightNumbers.RECUPERACAO_DEFESA.value} ST)")
            lutador.stamina = min(lutador.stamina_max, lutador.stamina + FightNumbers.RECUPERACAO_STAMINA.value)

        return relatorio, dano_usuario

    def pagar_habilidade(self, lutador, habilidade, relatorio):
        # Desconta a stamina e retorna a habilidade, ou None se o lutador não puder usá-la.
        if habilidade is None:
            return None
        if not lutador.pode_usar(habilidade):
            relatorio.append(f"O {lutador.apelido} não tem stamina suficiente para usar {habilidade.nome}")
            return None
        lutador.stamina -= habilidade.custo
        return habilidade

    def calcular_dano(self,atacante, habilidade_atacante, defensor, habilidade_defensor, relatorio):
        if habilidade_atacante is None or habilidade_atacante.tipo != 'Ataque':
            return 0
        dano = atacante.forca + habilidade_atacante.dano

        if habilidade_defensor is not None and habilidade_defensor.tipo == 'Esquiva':
            chance_desvio = min(habilidade_defensor.taxa_esquiva + defensor.esquiva, FightNumbers.TAXA_MAXIMA.value)
            if randint(1, 100) <= chance_desvio:
                relatorio.append(f"O {defensor.apelido} esquivou do {habilidade_atacante.nome} "
                                 f"do {atacante.apelido}! ({chance_desvio}% de chance)")
                return 0
            relatorio.append(f"O {defensor.apelido} tentou esquivar, mas não conseguiu!")
        elif habilidade_defensor is not None and habilidade_defensor.tipo == 'Defesa':
            taxa_defesa = min(habilidade_defensor.taxa_defesa + defensor.defesa, FightNumbers.TAXA_MAXIMA.value)
            dano = dano * (1 - taxa_defesa / 100)
            relatorio.append(f"O {defensor.apelido} bloqueou {taxa_defesa}% do golpe")

        dano = round_dano(dano)
        relatorio.append(f"O {atacante.apelido} acertou {habilidade_atacante.nome} e causou {dano} de dano "
                         f"no {defensor.apelido}")
        return dano

    def escolher_habilidade_cpu(self, lutador):
        # A CPU sorteia entre as habilidades que consegue pagar; sem stamina, descansa (None).
        lista_habilidades = self.__controlador_central.controlador_habilidade.habilidades
        possiveis = [habilidade for habilidade in lista_habilidades if lutador.pode_usar(habilidade)]
        if len(possiveis) == 0:
            return None
        return choice(possiveis)

    def simular_luta(self, boxeador_um, boxeador_dois):
        # Luta entre dois boxeadores da CPU, sem telas. Retorna o boxeador vencedor.
        controlador_boxeador = self.__controlador_central.controlador_boxeador
        lutador_um = EstadoLutador(boxeador_um, controlador_boxeador.caracteristicas_de_luta(boxeador_um))
        lutador_dois = EstadoLutador(boxeador_dois, controlador_boxeador.caracteristicas_de_luta(boxeador_dois))
        for jogada in range(FightNumbers.ROUNDS.value * FightNumbers.JOGADAS_POR_ROUND.value):
            self.resolver_turno(lutador_um, self.escolher_habilidade_cpu(lutador_um),
                                lutador_dois, self.escolher_habilidade_cpu(lutador_dois))
            if lutador_um.vida <= 0 or lutador_dois.vida <= 0:
                break
        return self.decidir_vencedor(lutador_um, lutador_dois).boxeador

    def busca_por_id(self, id, lista_habilidades):
        for habilidade in lista_habilidades:
            if habilidade.id == id:
                return habilidade
        return None

    def mostrar_luta(self, usuario, cpu, round, nome_fase=''):
        boxeador_um = usuario.boxeador
        boxeador_dois = cpu.boxeador
        return self.__tela_jogo.tela_luta_padrao(usuario.vida, cpu.vida,
                                                 usuario.stamina, cpu.stamina,
                                                 boxeador_um.nacionalidade, boxeador_dois.nacionalidade,
                                                 boxeador_um.nome, boxeador_dois.nome,
                                                 boxeador_um.apelido, boxeador_dois.apelido,
                                                 round, FightNumbers.ROUNDS.value, nome_fase)

    def mostrar_e_escolher_habilidade(self, usuario, cpu, mensagem_habilidade_escolhida, habilidades_boxeador_usuario):
        return self.__tela_jogo.tela_luta_escolha_habilidade(usuario.vida, cpu.vida,
                                                             usuario.stamina, cpu.stamina,
                                                             mensagem_habilidade_escolhida,
                                                             habilidades_boxeador_usuario)

    def retorna_informacoes_lista(self, lista, dano_total_causado):
        habilidades_usadas = len(lista)
        self.__tela_jogo.mostra_informacoes_luta_usuario(dano_total_causado, habilidades_usadas)


def round_dano(valor):
    return round(valor, 1)
