"""Posicionamento e escala das janelas do jogo.

O FreeSimpleGUI centraliza cada janela na área total da tela. Com dois monitores lado a lado
essa área é a soma dos dois, e o centro cai bem na divisa entre eles, então as janelas
"pulavam" de um monitor para o outro. Aqui escolhemos um único monitor (o que está com o
mouse quando o jogo abre) e todas as janelas e popups passam a nascer no centro dele.
"""
import io
import os
from functools import lru_cache

import FreeSimpleGUI as sg
from PIL import Image

PASTA_IMAGENS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Imagens')

ALTURA_PADRAO = 1080              # usada se não for possível detectar o monitor
PROPORCAO_IMAGEM_LUTA = 0.40      # altura da imagem da luta em relação à altura do monitor
PROPORCAO_IMAGEM_CAMPEAO = 0.50


class Monitor:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    @property
    def centro(self):
        return self.x + self.largura // 2, self.y + self.altura // 2

    def contem(self, ponto):
        px, py = ponto
        return self.x <= px < self.x + self.largura and self.y <= py < self.y + self.altura


class _Exibicao:
    def __init__(self):
        self.monitor = None
        self.deslocamento = (0, 0)

    def detectar(self):
        # Lê do Tk o tamanho de tela que o FreeSimpleGUI usa para centralizar e a posição do mouse.
        import tkinter
        raiz = tkinter.Tk()
        raiz.withdraw()
        largura_tk, altura_tk = raiz.winfo_screenwidth(), raiz.winfo_screenheight()
        mouse = raiz.winfo_pointerxy()
        raiz.destroy()

        self.monitor = self.escolher_monitor(mouse) or Monitor(0, 0, largura_tk, altura_tk)
        centro_x, centro_y = self.monitor.centro
        # O FreeSimpleGUI coloca a janela no centro da área do Tk e soma este deslocamento.
        self.deslocamento = (centro_x - largura_tk // 2, centro_y - altura_tk // 2)

    def escolher_monitor(self, mouse):
        try:
            from screeninfo import get_monitors
            monitores = [Monitor(m.x, m.y, m.width, m.height) for m in get_monitors()]
            principal = [Monitor(m.x, m.y, m.width, m.height) for m in get_monitors() if m.is_primary]
        except Exception:
            return None
        for monitor in monitores:
            if monitor.contem(mouse):
                return monitor
        if principal:
            return principal[0]
        return monitores[0] if monitores else None


_exibicao = _Exibicao()


def configurar_janelas():
    """Deve ser chamada uma vez, antes de abrir a primeira janela do jogo."""
    _exibicao.detectar()

    # Toda janela sem posição explícita (inclusive popups) nasce centralizada no monitor escolhido.
    init_original = sg.Window.__init__
    if getattr(init_original, '_punch_club', False):
        return

    def init_centralizado(self, *args, **kwargs):
        sem_posicao = kwargs.get('location') in (None, (None, None))
        sem_relativa = kwargs.get('relative_location') in (None, (None, None))
        if sem_posicao and sem_relativa:
            kwargs['relative_location'] = _exibicao.deslocamento
        init_original(self, *args, **kwargs)

    init_centralizado._punch_club = True
    sg.Window.__init__ = init_centralizado


def altura_monitor():
    return _exibicao.monitor.altura if _exibicao.monitor else ALTURA_PADRAO


@lru_cache(maxsize=None)
def imagem(nome_arquivo, proporcao_altura):
    """Retorna a imagem em PNG (bytes) redimensionada para uma fração da altura do monitor."""
    altura = int(altura_monitor() * proporcao_altura)
    with Image.open(os.path.join(PASTA_IMAGENS, nome_arquivo)) as original:
        largura = int(original.width * altura / original.height)
        redimensionada = original.resize((largura, altura), Image.LANCZOS)
        buffer = io.BytesIO()
        redimensionada.save(buffer, format='PNG')
    return buffer.getvalue()


def imagens_luta():
    return [imagem(nome, PROPORCAO_IMAGEM_LUTA) for nome in ('luta_1.png', 'luta_2.png', 'luta_3.png')]


def imagem_campeao():
    return imagem('campeao.png', PROPORCAO_IMAGEM_CAMPEAO)
