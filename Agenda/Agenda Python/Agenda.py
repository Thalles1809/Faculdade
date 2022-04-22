# Função que verifica se a variável já existe no sistema
def ext_contatos_cadastrados_nome(lista_de_contatos, nome):
    if len(lista_de_contatos) > 0:
        for contatos_cadastrados in lista_de_contatos:
            if contatos_cadastrados['nome'] == nome:
                return True
    return False

# Função que add contatos no sistema por dicionário dentro de uma lista

def novo_contato(lista_de_contatos):
    while True:
        nome = str(input("Digite o nome do contato: ")).lower()
        if not ext_contatos_cadastrados_nome(lista_de_contatos, nome):
            break
        else:
            print("Nome já utilizado!\nInsira outro nome")

    contatos_cadastrados = {
        'nome': nome,
        'telefone': str(input("Telefone: ")).lower(),
        'email': str(input("E-mail: ")).lower(),
        'twitter': str(input("Twitter: ")).lower(),
        'instagram': str(input("Instagram: ")).lower()}
    lista_de_contatos.append(contatos_cadastrados)
    print(
        f"O contato {contatos_cadastrados['nome']} foi cadastrado com sucesso!\n")

# Função que coloco novos dados para alterar o contato

def inserir_novos_dados(contatos_cadastrados):
    contatos_cadastrados['nome'] = str(input(" Novo nome: ")).lower()
    contatos_cadastrados['telefone'] = input(" Telefone do contato: ").lower()
    contatos_cadastrados['email'] = input(" E-mail do contato: ").lower()
    contatos_cadastrados['twitter'] = input(" Twitter do contato: ").lower()
    contatos_cadastrados['instagram'] = input(
        " Instagram do contato: ").lower()

    print(
        f"\nOs dados do contato {contatos_cadastrados['nome']}, foram alterados com suceso!\n")

# Função que modifica o contato apartir do nome

def modificar(lista_de_contatos):
    if len(lista_de_contatos) > 0:
        nome = str(input(" O nome do contato a ser alterado: ")).lower()
        if ext_contatos_cadastrados_nome(lista_de_contatos, nome):
            for contatos_cadastrados in lista_de_contatos:
                if contatos_cadastrados['nome'] == nome:
                    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"Nome: {contatos_cadastrados['nome']}")
                    print(f"Telefone: {contatos_cadastrados['telefone']}")
                    print(f"Email: {contatos_cadastrados['email']}")
                    print(f"Twitter: {contatos_cadastrados['twitter']}")
                    print(f"Instagram: {contatos_cadastrados['instagram']}")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    inserir_novos_dados(contatos_cadastrados)
                    break
        else:
            print(f"Não existe contato cadastrado com o nome informado {nome}")
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("    Nenhum contato cadastrado no sistema!      \n")

# Função que deleta um contato já cadastrado no sistema

def Deletar(lista_de_contatos):
    if len(lista_de_contatos) > 0:
        nome = str(input("Digite o nome do contato a ser excluído: ")).lower()
        if ext_contatos_cadastrados_nome(lista_de_contatos, nome):
            for i, contatos_cadastrados in enumerate(lista_de_contatos):
                if contatos_cadastrados["nome"] == nome:
                    print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"Nome: {contatos_cadastrados['nome']}")
                    print(f"Telefone: {contatos_cadastrados['telefone']}")
                    print(f"Email: {contatos_cadastrados['email']}")
                    print(f"Twitter: {contatos_cadastrados['twitter']}")
                    print(f"Instagram: {contatos_cadastrados['instagram']}")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

                    del lista_de_contatos[i]
                    print("O contato foi apagado com sucesso!")
                    break

        else:
            print(f"Não existe contato solicitado com o nome: {nome}\n")
    else:
        print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("    Nenhum contato cadastrado no sistema!      \n")

# Função que encontra contatos

def Encontrar(lista_de_contatos):
    if len(lista_de_contatos) > 0:
        nome = input("Digite o nome do contato a ser encontrado: ").lower()
        if ext_contatos_cadastrados_nome(lista_de_contatos, nome):
            for contatos_cadastrados in lista_de_contatos:
                if contatos_cadastrados["nome"] == nome:
                    print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print(f"Nome: {contatos_cadastrados['nome']}")
                    print(f"Telefone: {contatos_cadastrados['telefone']}")
                    print(f"Email: {contatos_cadastrados['email']}")
                    print(f"Twitter: {contatos_cadastrados['twitter']}")
                    print(f"Instagram: {contatos_cadastrados['instagram']}")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    break
        else:
            print(
                f"Não existe contato cadastrado no sistema com o email {nome}.\n")
    else:
        print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("    Nenhum contato cadastrado no sistema!      \n")

# Função que mostra todos os contatos cadastrados

def listar(lista_de_contatos):
    if len(lista_de_contatos) > 0:
        for i, contatos_cadastrados in enumerate(lista_de_contatos):
            print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Contato {i+1}:")
            print(f"\tNome: {contatos_cadastrados['nome']}")
            print(f"\tTelefone: {contatos_cadastrados['telefone']}")
            print(f"\tEmail: {contatos_cadastrados['email']}")
            print(f"\tTwitter: {contatos_cadastrados['twitter']}")
            print(f"\tInstagram: {contatos_cadastrados['instagram']}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    else:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("    Nenhum contato cadastrado no sistema!      \n")

# Função que referência o menu para ser executado, juntamente com a condicionais if

def prompt():
    lista_de_contatos = []

    while True:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("!!!!!     Agenda Telefônica     !!!!!")
        print("!!!!! 1 - Novo contato          !!!!!")
        print("!!!!! 2 - Modificar contato     !!!!!")
        print("!!!!! 3 - Deletar contato       !!!!!")
        print("!!!!! 4 - Encontrar contato     !!!!!")
        print("!!!!! 5 - Mostrar todos contato !!!!!")
        print("!!!!! 6 - Finalizar             !!!!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        while True:
            try:
                escolha = int(input("\nEscolha uma das alternativas >>> "))
                break
            except ValueError:
                print("\nApenas números!\n")

        if escolha == 1:
            novo_contato(lista_de_contatos)

        elif escolha == 2:
            modificar(lista_de_contatos)

        elif escolha == 3:
            Deletar(lista_de_contatos)

        elif escolha == 4:
            Encontrar(lista_de_contatos)

        elif escolha == 5:
            listar(lista_de_contatos)

        elif escolha == 6:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Programa finalizado !\n")
            break
        else:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Inválido\n")


prompt()
