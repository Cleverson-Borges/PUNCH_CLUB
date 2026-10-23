class Luta:
    # A luta guarda apenas os CPFs dos boxeadores: os objetos ficam no BoxeadorDAO,
    # assim o torneio salvo não carrega cópias desatualizadas dos lutadores.
    def __init__(self, cpf_boxeador_um: int, cpf_boxeador_dois: int):
        self.__cpf_boxeador_um = cpf_boxeador_um
        self.__cpf_boxeador_dois = cpf_boxeador_dois
        self.__cpf_vencedor = None

    @property
    def cpf_boxeador_um(self):
        return self.__cpf_boxeador_um

    @property
    def cpf_boxeador_dois(self):
        return self.__cpf_boxeador_dois

    @property
    def cpf_vencedor(self):
        return self.__cpf_vencedor

    @property
    def finalizada(self):
        return self.__cpf_vencedor is not None

    @cpf_boxeador_um.setter
    def cpf_boxeador_um(self, cpf):
        if isinstance(cpf, int):
            self.__cpf_boxeador_um = cpf
        else:
            raise TypeError('O CPF do lutador deve ser um inteiro')

    @cpf_boxeador_dois.setter
    def cpf_boxeador_dois(self, cpf):
        if isinstance(cpf, int):
            self.__cpf_boxeador_dois = cpf
        else:
            raise TypeError('O CPF do lutador deve ser um inteiro')

    @cpf_vencedor.setter
    def cpf_vencedor(self, cpf):
        if cpf in (self.__cpf_boxeador_um, self.__cpf_boxeador_dois):
            self.__cpf_vencedor = cpf
        else:
            raise ValueError('O vencedor deve ser um dos lutadores da luta')

    def envolve(self, cpf):
        return cpf in (self.__cpf_boxeador_um, self.__cpf_boxeador_dois)
