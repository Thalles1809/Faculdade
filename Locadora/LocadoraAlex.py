# class Carro:#ISSO TEM Q FICAR AMOSTRA QND ACESSA adicionar novos carros, AINDA NAO FUNCIONA
#    Numero = 1
#    Categoria = 'SUV'
#    Transmissão = 'Automática'
#    Combustivel = 'Flex'
#    Marca = 'Ford'
#    Modelo = 'EcoEsport'


def adiciona_novos_carros():  # bloco para adicionar carros

    print('Preencha o que é pedido.')
    banco_de_dados['Categoria'] = str(input('Digite a categoria: '))
    banco_de_dados['Transmissão'] = str(input('Digite a transmissão: '))
    banco_de_dados['Combustivel'] = str(input('Digite o combustivel: '))
    banco_de_dados['Marca'] = str(input('Digite a marca: '))
    banco_de_dados['Modelo'] = str(input('Digite o modelo: '))

    lista.append(banco_de_dados.copy())


def locar_veiculo():  # aqui deve aparecer uma lista de carros que estão disponiveis para locação
    for i in range():
        # e para aparecer uma lista de carros pra locar, escolher um e conseguir diminuir um da primeira lista
        print(lista[i])
    # ainda nao esta funcionando como deveria.


# class Cliente:#ISSO TEM Q FICAR AMOSTRA QND ACESSA CLIENTE, AINDA NAO FUNCIONA
#    Nome = 'José da Silva'
#    CPF = 89775452
#    RG = 789546

def Cadastrar_Novo_Cliente():  # bloco para adicionar clientes

    print('Preencha o que é pedido.')
    banco_de_dados2['Nome:'] = str(input('Digite seu nome: '))
    banco_de_dados2['CPF:'] = int(input('Digite seu CPF: '))
    banco_de_dados2['RG:'] = int(input('Digite seu RG: '))

    lista2.append(banco_de_dados2.copy())


def Cliente():  # bloco para saber se esse cliente pode alugar carro

    print('Vamos verificar seus dados. Por favor preencha os campos abaixo.')
    cliente_cadastrado['Nome:'] = str(input('Digite seu nome: '))
    cliente_cadastrado['CPF:'] = int(input('Digite seu CPF: '))
    cliente_cadastrado['RG:'] = int(input('Digite seu RG: '))

    lista3.append(cliente_cadastrado.copy())


lista = list({'Categoria:' 'SUV', 'Transmissão:' 'Automática', 'Combustível:' 'Flex',
             'Marca:' 'Ford', 'Modelo:' 'EcoSport'})  # lista para carro
banco_de_dados = dict()  # dicionario para carro

lista2 = list({'Nome:' 'José da Silva', 'CPF:' '89775452',
              'RG:' '789546'})  # lista para cliente
banco_de_dados2 = dict()  # dicionario para cliente

lista3 = list()
cliente_cadastrado = dict()  # se o cliente_cadastrado for igual ao lista2


while True:
    print('='*78)
    print('-=-=-= Bem-vindo a Locadora Boa Viagem, escolha uma das oopções abaixo: -=-=-=')
    print('='*78)
    print('1 - Cadastrar um Novo Veiculo')  # funcionando
    # funcionando pela metade tem que criar outro banco e lista para clientes
    print('2 - Cadastrar um Novo Cliente')
    print('3 - Realizar a locação de um Veiculo')
    print('4 - Relatório de locação')  # funcionando
    print('='*78)

    while True:  # aqui tem uma validação
        try:
            menu = int(input('Digite o numero de uma opcao acima: '))
            break
        except ValueError:
            print("Oops! Você digitou algo errado, tente novamente.")

    if menu == 1:  # aqui adiciona carros
        adiciona_novos_carros()
        print(banco_de_dados)

    elif menu == 2:  # aqui adiciona clientes
        Cadastrar_Novo_Cliente()
        print(banco_de_dados2)

    elif menu == 3:  # verifica se o cliente existe ,se sim vai pra locar veiculo se nao vai pra cadastro de cliente
        Cliente()
        if lista3 == lista2:  # eu acho q aqui deveria ter um loop pra vasculhar em toda a lista2
            locar_veiculo()
        else:
            Cadastrar_Novo_Cliente()

    elif menu == 4:  # aqui mosta tudo que foi adicionado nas listas e depois sai do programa.
        print(lista, lista2, lista3)
        # break
