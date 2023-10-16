from abc import ABC, abstractmethod


class TelaAbstrata(ABC):

    @abstractmethod
    def le_str_valida(self):
        pass

    @abstractmethod
    def le_num_inteiro(self):
        pass

    @abstractmethod
    def le_num_inteiro_entre(self):
        pass

    @abstractmethod
    def le_num_float_entre(self):
        pass
