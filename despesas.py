def leiaInt(msg):
    # Ler um número inteiro.
    while True:
        try:
            n = int(input(msg))
        # Caso o usúario interropar de maneira drástica o programa durante a leitura do número inteiro, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('\nERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        # Caso o valor digitado não seja inteiro, uma mensagem de erro será exibida.
        except ValueError:
            print('ERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        else:
            # Caso o valor inteiro digitado seja menor que 0, uma mensagem de erro será exibida.
            if n < 0:
                print('ERRO! OPÇÃO INVÁLIDA')
                print('-' * 50)
            else:
                # Retorna o valor.
                return n


def leiaStr(msg):
    # Ler uma string.
    try:
        # Loop infinito.
        while True:
            # Tira os espaços do início e do final e capitaliza a primeira letra de cada palavra.
            nome_des = str(input(msg)).strip().title()
            # Tira todos os espaços.
            nome_sem_space = ''.join(nome_des.split())
            # Verifica se o valor digitado só contém letras do alfabeto.
            if nome_sem_space.isalpha():
                # Se sim, retorna o valor.
                return nome_des
            else:
                # Se não, uma mensagem de erro será exibida.
                print('ERRO! NOME INVÁLIDO')
                print('-' * 50)
    # Caso o usúario interropar de maneira drástica o programa durante a leitura do valor em string, uma mensagem de erro será exibida.
    except KeyboardInterrupt:
        print('\nERRO! OPÇÃO INVÁLIDA')
        print('-' * 50)


def leiaFloat(msg):
    # Loop infinito.
    while True:
        # Ler um número de ponto flutuante
        try:
            din = float(input(msg))
            # Transformar o valor em string e faz uma lista, separador a parte inteira da decimal.
            din_str = str(din).split('.')
        # Caso o valor digitado não seja um número de ponto flutuante, uma mensagem de erro será exibida.
        except ValueError:
            print('ERRO! VALOR INVÁLIDO')
            print('-' * 50)
        # Caso o usúario interropar de maneira drástica o programa durante a leitura do número de ponto flutuante, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('ERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        else:
            # Verifica se a parte decimal é maior que 2 ou se o valor é digitado é um número de ponto flutuante. Caso uma dessas alternativas ocorra, uma mensagem de erro será exibida.
            if len(din_str[1]) > 2 or din_str[0].isnumeric() == False:
                print('ERRO! VALOR INVÁLIDO')
                print('-' * 50)
            else:
                # Retorna o valor.
                return din


def menu(* opcoes):
    # Menu
    print('-' * 50)
    print('Analisador de Despesas'.center(50))
    print('-' * 50)
    for i, op in enumerate(opcoes):
        print(f'{i + 1} - {op}')
    print('-' * 50)
    # Loop infinito
    while True:
        # Chama a função leiaInt.
        num = leiaInt('Qual opção você deseja? ')
        # Verifica se o número digitado é maior que o tanto de opções ou se o valor é menor que um. Caso uma dessas alternativas ocorra, uma mensagem de erro será exibida.
        if num > len(opcoes) or num < 1:
            print('ERRO! OPÇÃO INVÁLIDA')
            print('-' * 50)
        else:
            # Retorna o valor.
            return num


def cadastrar():
    # Importandor a biblioteca json.
    import json
    # Dicionário e listas, feitos para que possamos organizar melhor as informações.
    info = {}
    lista_maior = []
    lista_menor = []
    print('-' * 50)
    # Pega o nome e o custo da despesa e adiciona no diciónario.
    info['Nome da Despesa'] = leiaStr('Nome da despesa: ')
    print('-' * 50)
    info['Custo da Despesa'] = leiaFloat('Custo da despesa: R$')
    # Cria uma cópia do diciónario e adiciona na lista menor.
    lista_menor.append(info.copy())
    # Cria uma cópia da lista menor e adiciona na lista maior.
    lista_maior.append(lista_menor[:])
    try:
        # Cria o arquivo e adiciona as informações.
        with open('despesas.json', 'x', encoding='utf-8') as arquivo:
            json.dump(lista_maior, arquivo, indent=4, ensure_ascii=False)
    except:
        try:
            # Ler o arquivo.
            with open('despesas.json', 'r', encoding='utf-8') as arquivo:
                # Transforma ele num objeto python.
                dados = json.load(arquivo)
                # Adiciona as novas informarções.
                dados.append(lista_menor)
        except:
            # Caso o arquivo já exista, mas não há nenhuma informação, ele será reescrito com as novas informações
            with open('despesas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(lista_maior, arquivo, indent=4, ensure_ascii=False)
        else:
            # Reescreve o arquivo com as novas informações.
            with open('despesas.json', 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    # Mensagem confirmação.
    print('-' * 50)
    print(
        f'Cadastro da Despesa "{info['Nome da Despesa']}" Concluído'.upper().center(50))


def exibir():
    # Importando as bibliotecas json e matplotlib.
    import json
    import matplotlib.pyplot as plt
    # Loop infinito.
    while True:
        # Listas que possuem os nomes e custos de cada despesa.
        nome_categorias = []
        valores = []
        try:
            # Ler um arquivo.
            with open('despesas.json', 'r', encoding='utf-8') as arquivo:
                # Transforma ele num objeto python.
                dados = json.load(arquivo)
        except:
            # Caso não tenha nenhuma despesa, uma mensagem de erro será exibida, e o loop infinito se quebrá.
            print('-' * 50)
            print('NENHUMA DESPESA CADASTRADA'.center(50))
            break
        else:
            if len(dados) == 0:
                # Caso não tenha nenhuma despesa, uma mensagem de erro será exibida, e o loop infinito se quebrá.
                print('-' * 50)
                print('NENHUMA DESPESA CADASTRADA'.center(50))
                break
            # Adiciona as informações nas listas.
            for nome_dados in dados:
                nome_categorias.append(nome_dados[0]['Nome da Despesa'])
                valores.append(nome_dados[0]['Custo da Despesa'])
        # Construção do gráfico.
        plt.pie(valores, labels=nome_categorias, autopct='%1.1f%%', wedgeprops={
                'edgecolor': 'white', 'linewidth': 2}, startangle=180, shadow=True, textprops={'fontsize': 10, 'color': 'black'}, center=(0, 0.7))
        # Titulo do gráfico.
        plt.title('Distribuição de Despesas Mensais')
        # Exibe o gráfico
        try:
            plt.show()
        # Caso o usúario interropar de maneira drástica o programa durante a exibição do gráfico, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            break
        break


def excluir():
    # Importar a biblioteca json.
    import json
    # Loop infinito.
    while True:
        try:
            # Ler um arquivo.
            with open('despesas.json', 'r', encoding='utf-8') as arquivo:
                # Transforma ele num objeto python.
                dados = json.load(arquivo)
        except:
            # Caso não tenha nenhuma despesa, uma mensagem de erro será exibida, e o loop infinito se quebrá.
            print('-' * 50)
            print('NENHUMA DESPESA CADASTRADA'.center(50))
            break
        else:
            # Caso não tenha nenhuma despesa, uma mensagem de erro será exibida, e o loop infinito se quebrá.
            if len(dados) == 0:
                print('-' * 50)
                print('NENHUMA DESPESA CADASTRADA'.center(50))
                break
            print('-' * 50)
            # Exibição das despesas.
            for indice, nome in enumerate(dados):
                for n in nome:
                    print(
                        f'{indice + 1} - {n['Nome da Despesa']}: R${n['Custo da Despesa']:.2f}')
            print('-' * 50)
            # Chama a função leiaInt.
            usu_res = leiaInt(
                'Qual despesa deseja excluir [0 PARA PARAR]? ')
            # Se o número for zero o loop se quebrará.
            if usu_res == 0:
                break
            # Se o número for maior que o tanto de despesas, uma mensagem de erro será exibida.
            if usu_res > len(dados):
                print('ERRO! OPÇÃO INVÁLIDA')
            else:
                for ind_escolhido, d in enumerate(dados):
                    # Verifica o índice.
                    if ind_escolhido == usu_res - 1:
                        # Mensagem de confirmação.
                        print(
                            f'DESPESA "{d[0]['Nome da Despesa']}" EXCLUÍDA'.upper())
                        # Deleta a despesa pelo índice.
                        del dados[ind_escolhido]
                        # Reescreve o arquivo.
                        with open('despesas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(dados, arquivo, indent=4,
                                      ensure_ascii=False)
