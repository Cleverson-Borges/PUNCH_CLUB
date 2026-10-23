# PUNCH_CLUB - The game for fighters

Jogo de boxe em turnos (inspirado em Clube da Luta e nas batalhas dos primeiros Pokémon),
desenvolvido por Breno Sayão e Cleverson Borges para a UFSC.

## Como rodar

Requer Python 3.10+ com Tkinter (no Ubuntu/Debian: `sudo apt install python3-tk`).

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

A interface usa o [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGUI), fork gratuito (LGPL)
do PySimpleGUI 4, que não exige licença.

As janelas abrem sempre centralizadas no monitor onde está o mouse quando o jogo inicia (útil com
monitor estendido), e as imagens se ajustam à resolução desse monitor. Isso usa `screeninfo` e `Pillow`
(ver `Telas/exibicao.py`).

## Regras

- **Boxeador**: ao criar, você distribui 10 pontos (força +1, esquiva +1, defesa +1, stamina +1, vida +2 por ponto)
  e escolhe 4 habilidades diferentes entre ataque, defesa e esquiva.
- **IMC**: durante as lutas, força, esquiva e stamina recebem ajustes conforme o IMC do boxeador
  (abaixo de 17, 17–18,49, 30–34,99 e 35 ou mais).
- **Luta**: 3 rounds de 3 jogadas. A cada jogada a CPU anuncia sua habilidade e você escolhe a sua.
  - Ataque causa `força + dano da habilidade`.
  - Defesa reduz o dano em `taxa da habilidade + defesa` (máx. 95%) e recupera stamina se ela estiver abaixo da metade.
  - Esquiva tem `taxa da habilidade + esquiva` (máx. 95%) de chance de anular o golpe.
  - Todos recuperam 4 de stamina por jogada. Vence quem zerar a vida do adversário ou terminar com mais vida.
  - Desistir conta como derrota.
- **Torneio**: 2, 4, 8 ou 16 lutadores em chave eliminatória. As lutas entre CPUs são simuladas.
  Cada vitória dá 5 pontos de característica. Entre as fases dá para parar, e o progresso fica salvo.

Os dados ficam em `boxeadores.pkl` e `torneios.pkl`.
