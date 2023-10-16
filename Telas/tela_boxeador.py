class TelaBoxeador:
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
    def cadastrar_boxeador(self):
        print('Cadastro de boxeador')
        nome = input('Nome: ')
        apelido = input('Apelido: ')
        idade = int(input('Idade: '))
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        nacionalidade = input('Nacionalidade: ')
        return {'nome': nome,
                'apelido': apelido,
                'idade': idade,
                'peso': peso,
                'altura': altura,
                'nacionalidade': nacionalidade}

    def tela_opcoes(self):
        print('-------- ░▒▓█ CADASTRO DE BOXEADOR █▓▒░ ----------',)
        print('Escolha sua opção:')
        print('(1) Incluir Boxeador')
        print('(2) Alterar Boxeador')
        print('(3) Listar Boxeador')
        print('(4) Excluir Boxeador')
        print('(5) Listar habilidades boxeador')
        print('(6) Listar caracteristicas boxeador')
        print('(0) Retornar')
        opcao = self.le_num_inteiro("Escolha a opcao: ", [0, 1, 2, 3, 4, 5, 6])
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def obtem_cpf(self):
        cpf = int(input('Por favor, insira o CPF: '))
        return cpf

    def verifica_boxeador_cpu(self):
        resposta = input('Este é o lutador que você quer jogar? (Responda com S (Sim) ou N (Não): ')
        return resposta

    def mostra_boxeador(self, dados_boxeador):
        print(f'NOME DO BOXEADOR: {dados_boxeador["nome"]}')
        print(f'CPF: {dados_boxeador["cpf"]}')
        print(f'APELIDO: {dados_boxeador["apelido"]}')
        print(f'IDADE: {dados_boxeador["idade"]} anos')
        print(f'PESO: {dados_boxeador["peso"]} kg')
        print(f'ALTURA: {dados_boxeador["altura"]} m')
        print(f'NACIONALIDADE: {dados_boxeador["nacionalidade"]}')
        print()

    def mostrar_habilidade_ataque(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Dano da habilidade: {habilidade.dano}")
        print()

    def mostrar_habilidade_defesa(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de Defesa: {habilidade.taxa_defesa}")
        print()

    def mostrar_habilidade_esquiva(self, habilidade):
        print(f"ID da habilidade: {habilidade.id}")
        print(f"Nome: {habilidade.nome}")
        print(f"Descrição: {habilidade.descricao}")
        print(f"Custo de Stamina: {habilidade.custo}")
        print(f"Taxa de esquiva: {habilidade.taxa_esquiva}")
        print()

    def mostrar_caracteristica_boxeador(self, caracteristica):
        print(f"Stamina: {caracteristica.stamina}")
        print(f"Esquiva: {caracteristica.esquiva}")
        print(f"Vida: {caracteristica.vida}")
        print(f"Força: {caracteristica.forca}")
        print(f"Defesa: {caracteristica.defesa}")
        print()

