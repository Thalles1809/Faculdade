def extCliente(listaCliente, cpf):
    if len(listaCliente) > 0:
        for cliente in listaCliente:
            if cliente['cpf'] == cpf:
                return True
    return False


def extVeiculo(listaVeiculo, placa):
    if len(listaVeiculo) > 0:
        for veiculo in listaVeiculo:
            if veiculo['placa'] == placa:
                return True
    return False


def novoCarro(listaVeiculo):
    print("\nInsira os dados do veículo:\n")
    placa = input("Digite a placa: ")
    veiculo = {}
    while True:
        try:
            categ = int(
                input("\n1 - Sedan\n2 - Picape\n3 - SUV\n\nEscolha uma categoria: "))
            break
        except ValueError:
            print("\nApenas números são aceitos!\n")

        while True:
            if categ == 1:
                categoria = ("sedan")
                break

            elif categ == 2:
                categoria = ("Picape")

            elif categ == 3:
                categoria = ("SUV")

            else:
                print("Opção inválida!\n")

    while True:
        try:
            trans = int(
                input("\n1 - Automática\n2 - Manual\n\nEscolha uma transmissão: "))
            break
        except ValueError:
            print("\nApenas números são aceitos!\n")

    while True:
        if trans == 1:
            transmissão = ("Automática")
            break

        elif trans == 2:
            transmissão = ("Manual")

        else:
            print("Opção inválida!")

    veiculo = {
        'categoria': categoria,
        'transmissão': transmissão,
        'combustível': combustível,
        'marca': marca,
        'Ano': int(input("Digite o ano: ")),
        'placa': placa,
    }


def novoCliente(listaCliente):
    print("\nNovo Cliente!\n")


def locarVeiculo(listaVeiculo, listaCliente):
    print("\nLocação\n")


def relatorioLocacao(listaCliente, listaVeiculo):
    print("\nRelatório de locação!\n")


def relatorioVeiculos(listaVeiculo):
    print("\nRelatório de Veículos!\n")


def relatorioClientes(listaCliente):
    print("\nRelatório de Cliente!\n")


def menu():

    listaVeiculo = []
    listaCliente = []

    while True:
        print("1 - Cadastrar novo veículo")
        print("2 - Cadastrar novo cliente")
        print("3 - Locação de veículo")
        print("4 - Relatório de locação")
        print("5 - Relatório de veículos cadastrados")
        print("6 - Relatório de clientes cadastrados")
        print("7 - Finalizar o programa !!!")

        while True:
            try:
                opc = int(input("\nDigite a opção desejada: "))
                break
            except ValueError:
                print("Oops! Opção inválida!")

        if opc == 1:
            novoCarro(listaVeiculo)

        elif opc == 2:
            novoCliente(listaCliente)

        elif opc == 3:
            locarVeiculo(listaVeiculo, listaCliente)

        elif opc == 4:
            relatorioLocacao(listaCliente, listaVeiculo)

        elif opc == 5:
            relatorioVeiculos(listaVeiculo)

        elif opc == 6:
            relatorioClientes(listaCliente)

        elif opc == 7:
            print("\nFinalizando o programa!!!\nObrigado pela preferência\n")
            break

        else:
            print("Opção inválida.")


menu()
