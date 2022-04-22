# -*- coding: utf-8 -*-
"""Agenda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bxogq-WLZ7hpYSfIC7TYR_poOK0SRIPo

*  Nome: Thalles Vinicius Franchin Peres Ladeira
*  Inscrição: 2172190004
*  Curso: Engenharia de Software

Função que recebe a variável nome para verificar se existe algum valor igual já cadastrado
"""

def ext_cnt_nome(lst, nome):
    if len(lst) > 0:
        for cnt in lst:
            if cnt['nome'] == nome:
                return True
    return False

"""Função que adiciona novos contatos para um dicionário que será inserida ao final de uma lista

"""

def adicionar(lst):
    while True:
        nome = str(input("Digite o nome do contato: ")).lower()
        if not ext_cnt_nome(lst, nome):
            break
        else:
            print("Nome já utilizado!\nInsira outro nome")

    cnt = {
        'nome': nome,
        'telefone': str(input("Telefone: ")).lower(),
        'email': str(input("E-mail: ")).lower(),
        'twitter': str(input("Twitter: ")).lower(),
        'instagram': str(input("Instagram: ")).lower()}
    lst.append(cnt)
    print(f"O contato {cnt['nome']} foi cadastrado com sucesso!\n")

"""Função que faz a inserção de novos dados em cadastro já inserido anteriormente"""

def inserir_novos_dados(cnt):
    cnt['nome'] = str(input(" Novo nome: ")).lower()
    cnt['telefone'] = input(" Telefone do contato: ").lower()
    cnt['email'] = input(" E-mail do contato: ").lower()
    cnt['twitter'] = input(" Twitter do contato: ").lower()
    cnt['instagram'] = input(" Instagram do contato: ").lower()

    print(
        f"\nOs dados do contato {cnt['nome']}, foram alterados com suceso!\n")

"""Função que busca o o valor pela chave do dicionário, mostra os atuais dados cadastrados e chama a função que cadastra os novos dados"""

def alterar(lst):
    if len(lst) > 0:
        nome = str(input(" O nome do contato a ser alterado: ")).lower()
        if ext_cnt_nome(lst, nome):
            for cnt in lst:
                if cnt['nome'] == nome:
                    print("\n##############################################")
                    print(f"Nome: {cnt['nome']}")
                    print(f"Telefone: {cnt['telefone']}")
                    print(f"Email: {cnt['email']}")
                    print(f"Twitter: {cnt['twitter']}")
                    print(f"Instagram: {cnt['instagram']}")
                    print("#############################################\n")

                    inserir_novos_dados(cnt)
                    break
        else:
            print(f"Não existe contato cadastrado com o nome informado {nome}")
    else:
        print("\n############################################")
        print("    Não existe contato a ser alterado!      ")
        print("############################################\n")

"""Função que executa a exclusão do cadastro por índice do dicionário na lista com a função for com enumerate"""

def excluir(lst):
    if len(lst) > 0:
        nome = str(input("Digite o nome do contato a ser excluído: ")).lower()
        if ext_cnt_nome(lst, nome):
            for i, cnt in enumerate(lst):
                if cnt["nome"] == nome:
                    print("\n##############################################")
                    print(f"Nome: {cnt['nome']}")
                    print(f"Telefone: {cnt['telefone']}")
                    print(f"Email: {cnt['email']}")
                    print(f"Twitter: {cnt['twitter']}")
                    print(f"Instagram: {cnt['instagram']}")
                    print("##############################################\n")

                    del lst[i]
                    print("O contato foi apagado com sucesso!")
                    break

        else:
            print(f"Não existe contato solicitado com o nome: {nome}\n")
    else:
        print("\n################################################")
        print("Não existe nenhum contato cadastrado no sistema! ")
        print("################################################\n")

"""Função para buscar se o contato e escreve-lo na tela"""

def buscar(lst):
    if len(lst) > 0:
        nome = input("Digite o nome do contato a ser encontrado: ").lower()
        if ext_cnt_nome(lst, nome):
            for cnt in lst:
                if cnt["nome"] == nome:
                    print("\n##############################################")
                    print(f"Nome: {cnt['nome']}")
                    print(f"Telefone: {cnt['telefone']}")
                    print(f"Email: {cnt['email']}")
                    print(f"Twitter: {cnt['twitter']}")
                    print(f"Instagram: {cnt['instagram']}")
                    print("##############################################\n")
                    break
        else:
            print(
                f"Não existe contato cadastrado no sistema com o email {nome}.\n")
    else:
        print("\n##############################################")
        print("    Nenhum contato cadastrado no sistema!      ")
        print("##############################################\n")

"""Função para buscar todos os cadastros e escreve-los em tela com a contagem de quantos cadastros"""

def listar(lst):
    if len(lst) > 0:
        for i, cnt in enumerate(lst):
            print("\n##############################################")
            print(f"Contato {i+1}:")
            print(f"\tNome: {cnt['nome']}")
            print(f"\tTelefone: {cnt['telefone']}")
            print(f"\tEmail: {cnt['email']}")
            print(f"\tTwitter: {cnt['twitter']}")
            print(f"\tInstagram: {cnt['instagram']}")
            print("##############################################\n")
    else:
        print("\n###################################################")
        print(" Não existe nenhum contato cadastrado para listar! ")
        print("###################################################\n")

"""Função matriz que contém o menu, e as condicioanis que vazem a verificação da opção escolhida pelo usuário"""

def main_menu():
    lst = []

    while True:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("---------------------------------")
        print("#####   Agenda Telefônica   #####")
        print("##### 1 - Adicionar contato #####")
        print("##### 2 - Alterar contato   #####")
        print("##### 3 - Excluir contato   #####")
        print("##### 4 - Buscar contato    #####")
        print("##### 5 - listar contato    #####")
        print("##### 6 - Sair              #####")
        print("---------------------------------")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        while True:
            try:
                opc = int(input("\nEscolha uma das opções a seguir ~> "))
                break
            except ValueError:
                print("\nAceito apenas números!\n")

        '''
        Forma de evitar o erro da digitação de caractere
        by: Monitor Samuel
        '''

        if opc == 1:
            adicionar(lst)

        elif opc == 2:
            alterar(lst)

        elif opc == 3:
            excluir(lst)

        elif opc == 4:
            buscar(lst)

        elif opc == 5:
            listar(lst)

        elif opc == 6:
            print("\n###################################################")
            print("Saindo do Programa...\nExecução finalizada com sucesso !")
            print("###################################################\n")
            break
        else:
            print("\n###################################################")
            print("\nOpção inválida.Tente novamente!\n")
            print("###################################################\n")


main_menu()