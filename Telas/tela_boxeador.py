from Telas.tela_central import TelaAbstrata


class TelaBoxeador(TelaAbstrata):
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

    def le_num_inteiro_entre(self, mensagem=" ", min_valor=None, max_valor=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if (min_valor is not None and valor_int < min_valor) or (
                        max_valor is not None and valor_int > max_valor):
                    raise ValueError
                return valor_int
            except ValueError:
                print(f"Você deve ter no minímo {min_valor} anos e no maximo {max_valor} anos para poder participar.")

    def le_num_float_entre(self, mensagem=" ", min_valor=None, max_valor=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_float = float(valor_lido)
                if (min_valor is not None and valor_float < min_valor) or (
                        max_valor is not None and valor_float > max_valor):
                    raise ValueError
                return valor_float
            except ValueError:
                print(f"O valor deve estar entre {min_valor} e {max_valor}.")

    def le_str_valida(self, mensagem=" ", strs_validas=None):
        while True:
            valor_lido = input(mensagem)
            if len(valor_lido) == 3:
                if strs_validas and valor_lido not in strs_validas:
                    print("Valor incorreto!")
                    if strs_validas:
                        print("Valores válidos: ", ", ".join(strs_validas))
                else:
                    return valor_lido.upper()
            else:
                print("A string deve conter exatamente 3 letras.")

    def cadastrar_boxeador(self):
        print('Cadastro de boxeador')
        nome = str(input('Nome: '))
        apelido = str(input('Apelido: '))
        idade = self.le_num_inteiro_entre('Idade: ', 18, 100)
        peso = self.le_num_float_entre('Peso: ', 30, 150)
        altura = self.le_num_float_entre('Altura [metros]: ', 1.20, 2.30)
        nacionalidade = self.le_str_valida('Nacionalidade: ')
        print()
        return {'nome': nome,
                'apelido': apelido,
                'idade': idade,
                'peso': peso,
                'altura': altura,
                'nacionalidade': nacionalidade}

    def tela_opcoes(self):
        print()
        print('-------- ░▒▓█ CADASTRO DE BOXEADOR █▓▒░ ----------',)
        print('Escolha sua opção:')
        print('(1) Incluir Boxeador')
        print('(2) Alterar Boxeador')
        print('(3) Listar Boxeador')
        print('(4) Excluir Boxeador')
        print('(5) Listar habilidades boxeador')
        print('(6) Listar caracteristicas boxeador')
        print('(0) Retornar')
        print()
        opcao = self.le_num_inteiro("Informe a sua escolha: ", [0, 1, 2, 3, 4, 5, 6])
        print()
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def obtem_cpf(self):
        cpf = self.le_num_inteiro('Por favor, insira o CPF: ')
        print()
        return cpf

    def verifica_boxeador_cpu(self):
        resposta = input('Este é o lutador que você quer jogar? (Responda com S (Sim) ou N (Não): ')
        return resposta

    def mostra_boxeador(self, dados_boxeador):
        print()
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
