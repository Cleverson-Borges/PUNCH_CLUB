from Entidades.boxeador import Boxeador


class ViewBoxeador:
    def __init__(self, controlador_central):
        pass


    def tela_cadastro_boxeador(self):
        print('Cadastro de boxeador')
        nome = input('Nome: ')
        apelido = input('Apelido: ')
        idade = int(input('Idade: '))
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        nacionalidade = input('Nacionalidade: ')
        equipamento = input('Equipamento: ')
        status = input('Status: ')
        return {'nome': nome,
                'apelido': apelido,
                'idade': idade,
                'peso': peso,
                'altura': altura,
                'nacionalidade': nacionalidade,
                'equipamento': equipamento,
                'status': status}