def ExtCar(carList, placa):
    if len(carList) > 0:
        for car in carList:
            if car['placa'] == placa:
                return True
    return False


def ExtClient(clientList, cpf):
    if len(clientList) > 0:
        for dado in clientList:
            if dado['cpf'] == cpf:
                return True
    return False


def NewCar(carList):
    carro = {}
    global categoria
    categoria = ""
    transmissão = ""
    combustivel = ""

    print("\n")
    print("="*50)
    print("Insira os dados do veículo:")
    print("="*50)
    print("\n")

    while True:
        placa = str(input("Digite a placa: ")).upper()
        if not ExtCar(carList, placa):
            break
        else:
            print("\nPlaca já cadastrada!\nInsira outra placa.\n")

    ano = int(input("\nQual o ano: "))
    marca = str(input("\nQual a marca: ")).upper()
    modelo = str(input("\nQual o modelo: ")).upper()

    while True:
        try:
            ctg = int(
                input("\n1 - Sedan\n2 - Picape\n3 - SUV\n4 - RET\n\nEscolha uma categoria: "))
            break
        except ValueError:
            print("\nApenas números são aceitos!\n")

    if ctg == 1:
        categoria = "SEDAN"
    elif ctg == 2:
        categoria = "PICAPE"
    elif ctg == 3:
        categoria = "SUV"
    elif ctg == 4:
        categoria = "RET"
    else:
        print("\nOpção inválida!\n")

    while True:
        try:
            trns = int(
                input("\n1 - Automático\n2 - Manual\n\nEscolha uma transmissão: "))
            break
        except ValueError:
            print("\nApenas números são aceitos!\n")

    if trns == 1:
        transmissão = "AUTOMÁTICO"
    elif trns == 2:
        transmissão = "MANUAL"
    else:
        print("\nOpção inválida!\n")

    while True:
        try:
            cbst = int(input(
                "\n1 - Diesel\n2 - Álcool\n3 - Gasolina\n4 - Flex\n5 - GNV\n\nEscolha um combustível: "))
            break
        except ValueError:
            print("\nApenas números são aceitos!\n")

    if cbst == 1:
        combustivel = "DIESEL"
    elif cbst == 2:
        combustivel = "ÁLCOOL"
    elif cbst == 3:
        combustivel = "GASOLINA"
    elif cbst == 4:
        combustivel = "FLEX"
    elif cbst == 5:
        combustivel = "GNV"
    else:
        print("\nOpção inválida!\n")

    carro = {
        'placa': placa,
        'ano': ano,
        'categoria': categoria,
        'transmissao': transmissão,
        'combustivel': combustivel,
        'marca': marca,
        'modelo': modelo
    }
    carList.append(carro)
    print(f"A placa {carro['placa']} foi cadastrado com sucesso!\n")


def NewClient(clientList):
    cliente = {}

    print("\n")
    print("="*50)
    print("####   Novo Cliente   ####")
    print("="*50)
    print("\n")

    print("="*50)
    while True:
        cpf = str(input("Digite a cpf: ")).upper()
        if not ExtClient(clientList, cpf):
            break
        else:
            print("CPF já cadastrada!\nInsira outro CPF.\n")
    cliente = {
        'nome': str(input("\nDigite o nome: ")),
        'rg': str(input("Digite o RG: ")),
        'cpf': cpf
    }
    clientList.append(cliente)
    print(f"\nO cliente {cliente['nome']}, foi cadastrado com sucesso!\n")


def RentCar(carList, clientList):
    print("\n")
    print("="*50)
    print("####   Aluguel de Carro   ####")
    print("="*50)
    print("\n")


def RentReport(rentList):
    print("\n")
    print("="*50)
    print("####   Relatório de Aluguel   ####")
    print("="*50)
    print("\n")


def CarReport(carList):
    print("\n")
    print("="*50)
    print("####   Relatório dos Carros   ####")
    print("="*50)
    print("\n")

    if len(carList) > 0:
        for i, carro in enumerate(carList):
            print("="*50)
            print(f"Carro {i+1}:")
            print(f"\tPlaca: {carro['placa']}")
            print(f"\tAno: {carro['ano']}")
            print(f"\tCategoria: {carro['categoria']}")
            print(f"\tTransmissão: {carro['transmissao']}")
            print(f"\tCombustível: {carro['combustivel']}")
            print(f"\tMarca: {carro['marca']}")
            print(f"\tModelo: {carro['modelo']}")
            print("="*50)

        print(f"Quantidade total de carros é: {len(carList)}\n\n")

    else:
        print("="*50)
        print("Nenhum carro cadastrado no sistema! \n")


def ClientReport(clientList):
    print("\n")
    print("="*50)
    print("####   Relatório de Clientes   ####")
    print("="*50)
    print("\n")

    if len(clientList) > 0:
        for i, cliente in enumerate(clientList):
            print("="*50)
            print(f"Cliente {i+1}:")
            print(f"\tNome: {cliente['nome']}")
            print(f"\tRG: {cliente['rg']}")
            print(f"\tCPF: {cliente['cpf']}")
            print("="*50)

        print(f"Quantidade total de clientes é: {len(clientList)}\n\n")

    else:
        print("="*50)
        print("Nenhum cliente cadastrado no sistema! \n")


def Menu():
    carList = []
    clientList = []
    rentList = []

    while True:
        print("==================================================")
        print("####            Sistema Locadora              ####")
        print("==================================================")
        print("####   1 - Cadastrar novo veículo             ####")
        print("####   2 - Cadastrar novo cliente             ####")
        print("####   3 - Locação de veículo                 ####")
        print("####   4 - Relatório de locação               ####")
        print("####   5 - Relatório de veículos cadastrados  ####")
        print("####   6 - Relatório de clientes cadastrados  ####")
        print("####   7 - Finalizar o programa !!!           ####")
        print("==================================================")

        while True:
            try:
                opc = int(input("\nDigite a opção desejada: "))
                break
            except ValueError:
                print("\nOops, esse menu não aceita letras!\n")

        if opc == 1:
            NewCar(carList)

        elif opc == 2:
            NewClient(clientList)

        elif opc == 3:
            RentCar(carList, clientList)

        elif opc == 4:
            RentReport(rentList)

        elif opc == 5:
            CarReport(carList)

        elif opc == 6:
            ClientReport(clientList)

        elif opc == 7:
            print("\nFinalizando o programa!!!\n\nObrigado pela preferência\n")
            break

        else:
            print("\nOpção inválida!\n")


Menu()
