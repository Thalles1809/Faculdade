# Funções do programa
def ext_contato(lista, nome):
    if len(lista) > 0:
        for contato in lista:
            if contato['nome'] == nome:
                return True
    return False


def modificar_um_cadastro(lista):
    if len(lista) > 0:
        nome = str(input("Digite o e-mail do contato a ser alterado: "))
        if ext_contato(lista, nome):
            for contato in lista:
                if contato['nome'] == nome:
                    print("\n==============================================")
                    print(f"\tNome: {contato['nome']}")
                    print(f"\tTelefone: {contato['telefone']}")
                    print(f"\tEmail: {contato['email']}")
                    print(f"\tTwitter: {contato['twitter']}")
                    print(f"\tInstagram: {contato['instagram']}")
                    print("==============================================\n")


def remover_um_cadastro(lista):
    if len(lista) > 0:
        nome = str(input("Digite o e-mail do contato a ser excluído: "))
        if ext_contato(lista, nome):
            for i, contato in enumerate(lista):
                if contato["nome"] == nome:
                    print("\n==============================================")
                    print(f"Nome: {contato['nome']}")
                    print(f"Telefone: {contato['telefone']}")
                    print(f"Email: {contato['email']}")
                    print(f"Twitter: {contato['twitter']}")
                    print(f"Instagram: {contato['instagram']}")
                    print("==============================================\n")

                    del lista[i]
                    print("O contato foi apagado com sucesso!")
                    break

        else:
            print(f"Não existe contato solicitado com o e-mail {nome}\n")
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def consultar_um_cadastro(lista):
    if len(lista) > 0:
        nome = input("Digite o e-mail do contato a ser encontrado: ")
        if ext_contato(lista, nome):
            for contato in lista:
                if contato["nome"] == nome:
                    print("\n==============================================")
                    print("Nome: {}".format(contato["nome"]))
                    print("Telefone: {}".format(contato["telefone"]))
                    print("Email: {}".format(contato["email"]))
                    print("Twitter: {}".format(contato["twitter"]))
                    print("Instagram: {}".format(contato["instagram"]))
                    print("==============================================\n")
                    break
        else:
            print(
                f"Não existe contato cadastrado no sistema com o email {nome}.\n")
    else:
        print("Nenhum contato cadastrado no sistema.\n")


def lista_todos_os_contatos(lista):
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            print("\n==============================================")
            print(f"Contato {i+1}:")
            print(f"\tNome: {contato['nome']}")
            print(f"\tTelefone: {contato['telefone']}")
            print(f"\tEmail: {contato['email']}")
            print(f"\tTwitter: {contato['twitter']}")
            print(f"\tInstagram: {contato['instagram']}")
            print("==============================================\n")

        print(f"Quantidade total de contatos é: {len(lista)}\n")


def inicio_do_cadastro(lista):
    contato = {}
    while True:
        nome = str(input("Digite o nome do contato: "))
        if not ext_contato(lista, nome):
            break
        else:
            print("E-mail já ultilizado!\nInsira outro e-mail")

    contato = {
        'nome': nome,
        'email': str(input("Digite o e-mail do contato: ")),
        'telefone': str(input("Digite o telefone do contato: ")),
        'twitter': str(input("Digite o twitter: @")),
        'instagram': str(input("Digite o instagram: @"))
    }
    lista.append(contato)
    print("O contato {} foi cadastrado do sucesso!\n".format(contato['nome']))


def Inicializacao_do_programa():

    lista = []
    while True:
        print("==========================================")
        print("####       AGENDA TELEFÔNICA          ####")
        print("==========================================")
        print("####  1 - para cadastrar              ####")
        print("####  2 - para consultar um cadastro  ####")
        print("####  3 - para remover um cadastro    ####")
        print("####  4 - para modificar um cadastro  ####")
        print("####  5 - para listar                 ####")
        print("####  6 - para finalizar cadastro     ####")
        print("==========================================")

        while True:
            try:
                opc = int(input("\nEscolha uma opção acima: "))
                break
            except ValueError:
                print("\nApenas números são aceitos!\n")

            '''
            Código de exeção de erro by: Monitor Samuel
            '''

        if opc == 1:
            inicio_do_cadastro(lista)
        elif opc == 2:
            consultar_um_cadastro(lista)
        elif opc == 3:
            remover_um_cadastro(lista)
        elif opc == 4:
            modificar_um_cadastro(lista)

        elif opc == 5:
            lista_todos_os_contatos(lista)

        elif opc == 6:
            print("Cadastro encerrado, programa finalizado.")
            break
        else:
            print("Não há esta opção.")


Inicializacao_do_programa()
