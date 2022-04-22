class Locadora(object):

    def __init__(self):
        self.ListaCliente = []
        self.ListaCarro = []
        self.AluguelCarro = []
        self.menu()

    def menu(self):

        while True:
            print("Bem Vindo a locadora BOA VIADAGEM")
            print("1 - Cadastrar novo veículo")
            print("2 - Cadastrar novo cliente")
            print("3 - Locação de veículo")
            print("4 - Relatório de locação")
            print("5 - Busca de veículos cadastrados")
            print("6 - Busca de clientes cadastrados")
            print("7 - Relatório de veículos cadastrados")
            print("8 - Relatório de clientes cadastrados")
            print("9 - Alterar dados veículos cadastrados")
            print("10 - Alterar dados clientes cadastrados")
            print("11 - Finalizar o programa !!!")

            while True:
                try:
                    opc = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")

            if opc == 1:
                Carro.novo_carro(self)

            elif opc == 2:
                Cliente.novo_cliente(self)

                '''elif opc == 3:
                    

                elif opc == 4:'''

            elif opc == 5:
                Carro.buscar_carro(self)

            elif opc == 6:
                Cliente.buscar_cliente(self)

            elif opc == 7:
                Carro.listar_carro(self)

            elif opc == 8:
                Cliente.listar_cliente(self)

            elif opc == 9:
                Carro.alterar_carro(self)

            elif opc == 10:
                Cliente.alterar_cliente(self)

            elif opc == 11:
                print("\nFinalizado!!!")
                break

            else:
                print("\nInválido!\n")


class Carro(Locadora):
    def __init__(self, placa, ano, categoria, transmissao, combustivel, marca, modelo, alugado):
        self.placa = placa
        self.ano = ano
        self.categoria = categoria
        self.transmissao = transmissao
        self.combustivel = combustivel
        self.marca = marca
        self.modelo = modelo
        self.alugado = alugado

    def alterar_carro(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa : ")).upper()
            if Carro.existe_carro(self):
                for car in self.ListaCarro:
                    if car['placa'] == self.placa:
                        print(f"\n\tPlaca: {car['placa']}")
                        print(f"\tAno: {car['ano']}")
                        print(f"\tCategoria: {car['categoria']}")
                        print(f"\tTransmissão: {car['transmissao']}")
                        print(f"\tCombustível: {car['combustivel']}")
                        print(f"\tMarca: {car['marca']}")
                        print(f"\tModelo: {car['modelo']}")
                        print(f"\tAlugado: {car['alugado']}\n")

                        car['placa'] = str(input("Placa:")).upper()
                        car['ano'] = str(input("Ano:"))
                        car['categoria'] = str(
                            input("Opções:\nSedan\nPicape\nSUV\nDigite: ")).upper()
                        car['transmissao'] = str(
                            input("Opções:\nAutomático\nManual\nDigite: ")).upper()
                        car['combustivel'] = str(input(
                            "Opções:\nGasolina\nÁlcool\nFlex\nDiesel\nGNV\nDigite: ")).upper()
                        car['marca'] = str(input("Marca:")).upper()
                        car['modelo'] = str(input("modelo:")).upper()
                        car['alugado'] = int(
                            input("Opção:\n1 - Disponível\n2 - Alugado"))

                        print(f"Os dados da {self.placa} foram alterados")
                        break

            else:
                print(
                    f"Não existe veiculo cadastrado com a placa informado {self.placa}")
        else:
            print("Não existe veículo a ser alterado!")

    def listar_carro(self):
        if len(self.ListaCarro) > 0:
            for i, car in enumerate(self.ListaCarro):
                print(f"Carro {i+1}:")
                print(f"Placa: {car['placa']}")
                print(f"Ano: {car['ano']}")
                print(f"Categoria: {car['categoria']}")
                print(f"Transmissão: {car['transmissao']}")
                print(f"Combustível: {car['combustivel']}")
                print(f"Marca: {car['marca']}")
                print(f"Modelo: {car['modelo']}")
            print(f"Total de veículos é: {len(self.ListaCarro)}\n")
        else:
            print("\nNenhum veículo para listar! ")

    def buscar_carro(self):
        if len(self.ListaCarro) > 0:
            self.placa = str(input("Digite a placa: ")).upper()
            for car in self.ListaCarro:
                if car['placa'] == self.placa:
                    print(f"Placa: {car['placa']}")
                    print(f"Ano: {car['ano']}")
                    print(f"Categoria: {car['categoria']}")
                    print(f"Transmissão: {car['transmissao']}")
                    print(f"Combustível: {car['combustivel']}")
                    print(f"Marca: {car['marca']}")
                    print(f"Modelo: {car['modelo']}")
                    break
        else:
            print("Nenhum veiculo cadastrado")

    def existe_carro(self):
        if len(self.ListaCarro) > 0:
            for car in self.ListaCarro:
                if car['placa'] == self.placa:
                    return True
        return False

    def novo_carro(self):

        while True:
            self.placa = str(input("\n\nplaca: ")).upper()
            if not Carro.existe_carro(self):
                break
            else:
                print("\nJá cadastrado no sistema")
        self.ano = int(input("Ano: "))

        while True:
            print("1 - Sedan\n2 - Picape\n3 - SUV")
            while True:
                try:
                    ctg = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")

            if ctg == 1:
                self.categoria = "SEDAN"
                break
            elif ctg == 2:
                self.categoria = "PICAPE"
                break
            elif ctg == 3:
                self.categoria = "SUV"
                break
            else:
                print("\nInválida")

        while True:
            print("\n1 - Automático\n2 - Manual")
            while True:
                try:
                    trns = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("\nNão aceita letras!\n")

            if trns == 1:
                self.transmissao = "AUTOMATICO"
                break
            elif trns == 2:
                self.transmissao = "MANUAL"
                break
            else:
                print("\nInválida")

        while True:
            print("\n1 - Gasolina\n2 - Álcool\n3 - Flex\n4 - Diesel\n5 - GNV")
            while True:
                try:
                    cmbst = int(input("\nDigite: "))
                    break
                except ValueError:
                    print("Não aceita letras!\n")

            if cmbst == 1:
                self.combustivel = "GASOLINA"
                break
            elif cmbst == 2:
                self.combustivel = "ALCOOL"
                break
            elif cmbst == 3:
                self.combustivel = "FLEX"
                break
            elif cmbst == 4:
                self.combustivel = "DIESEL"
                break
            elif cmbst == 5:
                self.combustivel = "GNV"
                break
            else:
                print("\nInválida")

        self.marca = str(input("Digite a marca: ")).upper()
        self.modelo = str(input("Digite o modelo: ")).upper()
        self.alugado = "1"
        carro = {
            'placa': self.placa,
            'ano': self.ano,
            'categoria': self.categoria,
            'transmissao': self.transmissao,
            'combustivel': self.combustivel,
            'marca': self.marca,
            'modelo': self.modelo,
            'alugado': self.alugado
        }

        self.ListaCarro.append(carro)
        print(self.ListaCarro)


class Cliente(Locadora):

    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def listar_cliente(self):
        if len(self.ListaCliente) > 0:
            for i, clt in enumerate(self.ListaCliente):
                print(f"\nCliente {i+1}:")
                print(f"Nome: {clt['nome']}")
                print(f"CPF: {clt['cpf']}")
                print(f"RG: {clt['rg']}\n")
            print(f"Total de clientes é: {len(self.ListaCliente)}\n")
        else:
            print("\nNenhum cliente para listar!\n")

    def buscar_cliente(self):
        if len(self.ListaCliente) > 0:
            self.cpf = str(input("Digite o cpf: ")).upper()
            for car in self.ListaCliente:
                if car['cpf'] == self.cpf:
                    print(f"\nNome: {car['nome']}")
                    print(f"CPF: {car['cpf']}")
                    print(f"RG: {car['rg']}\n")
                    break
        else:
            print("\nNenhum cliente cadastrado no sistema!\n")

    def existe_cliente(self):
        if len(self.ListaCliente) > 0:
            for clt in self.ListaCliente:
                if clt['cpf'] == self.cpf:
                    return True
        return False

    def novo_cliente(self):
        while True:
            self.cpf = str(input("Digite o CPF: "))
            if not Cliente.existe_cliente(self):
                break
            else:
                print("Já cadastrado no sistema")
        self.nome = str(input("Nome do cliente: ")).upper()
        self.rg = str(input("RG: "))
        usuario = {
            'nome': self.nome,
            'cpf': self.cpf,
            'rg': self.rg
        }

        self.ListaCliente.append(usuario)
        print(self.ListaCliente)


Locadora()
