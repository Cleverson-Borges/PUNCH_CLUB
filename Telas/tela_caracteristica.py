class TelaCaracteristica:
    def __init__(self):
        pass

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)
    def tela_cadastro_status(self):
        forca = 10
        esquiva = 10
        vida = 100
        defesa = 10
        stamina = 10
        incremento_de_pontos = 10
        incremento_de_vida = 25
        print('Distribua os pontos do seu lutador')
        for i in range(10):
            print('Você tem {} pontos'.format(10 - i))
            print(f'1 - Força. Está com {forca} pontos de força')
            print(f'2 - Esquiva Está com {esquiva} pontos de esquiva')
            print(f'3 - Vida Está com {vida} pontos de vida')
            print(f'4 - Defesa Está com {defesa} pontos de defesa')
            print(f'5 - Stamina Está com {stamina} pontos de stamina')
            print('0 - Sair')
            opcao = self.le_num_inteiro("Escolha a opcao: ", [0, 1, 2, 3, 4, 5])
            if opcao == 1:
                forca = forca + incremento_de_pontos
            elif opcao == 2:
                esquiva = esquiva + incremento_de_pontos
            elif opcao == 3:
                vida = vida + incremento_de_vida
            elif opcao == 4:
                defesa = defesa + incremento_de_pontos
            elif opcao == 5:
                stamina = stamina + incremento_de_pontos
            elif opcao == 0:
                break

        return {'forca': forca,
                'esquiva': esquiva,
                'vida': vida,
                'defesa': defesa,
                'stamina': stamina}