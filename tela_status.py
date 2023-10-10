class ViewStatus:
    def __init__(self):
        pass

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
            print('6 - Sair')
            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                forca = forca + incremento_de_pontos
            elif opcao == 2:
                esquiva = esquiva + incremento_de_pontos
            elif opcao == 3:
                vida = vida + incremento_de_vida
            elif opcao == 4:
                defesa = defesa + incremento_de_pontos
            elif opcao == 4:
                stamina = stamina + incremento_de_pontos
            elif opcao == 5:
                break
            else:
                print('Opção inválida')

        return {'forca': forca,
                'esquiva': esquiva,
                'vida': vida,
                'defesa': defesa,
                'stamina': stamina}