from Controladores.controlador_central import ControladorCentral
from Telas.exibicao import configurar_janelas

if __name__ == "__main__":
  configurar_janelas()
  ControladorCentral().inicializa_sistema()