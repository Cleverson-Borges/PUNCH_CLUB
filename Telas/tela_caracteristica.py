from Telas.tela_central import TelaAbstrata


class TelaCaracteristica(TelaAbstrata):
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
                print("Valor inválido!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)
    def tela_cadastro_status(self):
        forca = 10
        esquiva = 10
        vida = 100
        defesa = 10
        stamina = 15
        incremento_de_pontos = 3
        incremento_de_vida = 10
        print('Distribua os pontos do seu lutador!')
        for i in range(10):
            print(f'Você tem {10 - i} ponto(s) para serem distribuídos')
            print()
            print(f'1 - Força   - [{forca}] pontos de força atualmente')
            print(f'2 - Esquiva - [{esquiva}] pontos de esquiva atualmente')
            print(f'3 - Vida    - [{vida}] pontos de vida atualmente')
            print(f'4 - Defesa  - [{defesa}] pontos de defesa atualmente')
            print(f'5 - Stamina - [{stamina}] pontos de stamina atualmente')
            print()
            print('0 - Sair')
            opcao = self.le_num_inteiro("Escolha uma opção: ", [0, 1, 2, 3, 4, 5])
            print()
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
