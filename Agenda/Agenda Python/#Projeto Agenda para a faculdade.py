def salvar_Contatos(pasta):# bloco de função onde cria um arquivo txt para salvar contatos
    arquivo = open('contatos.txt', 'write')#salva os contatos em um arquivo txt

    for contato in pasta:
        arquivo.write('{}#{}#{}#{}#{}\n'.format( contato['nome'],contato['email'], contato['telefone'], contato['twitter'], contato['instagram'],))

    arquivo.close()# so salva realmente quando fecha o arquivo aqui.

def carregar_Contatos():# bloco de função que vai carregar os contatos que estão salvos
    pasta = []

    try:
        arquivo = open('contatos.txt', 'r')#abri o arquivo txt e le esse arquivo.

        for linha in arquivo.readlines():
            coluna = linha.strip().split('#')

            contato = {#dicionario
                'twitter': coluna[0],
                'email': coluna[1],
                'telefone': coluna[2],
                'instagram': coluna[3],
                'nome': coluna[4]
            }
            pasta.append(contato)    
        arquivo.close()

    except FileNotFoundError:# retira um possivel erro
       pass 
    return pasta

def contatos_Existentes(pasta, email):# bloco de função de contatos existentes
    if len(pasta)>0:
        for contato in pasta:
            if contato['email'] == email:
                return True
    return False          

def adicionar(pasta):#bloco de função para adicionar novos contatos
    
    while True:
        email = input('Digite o e-mail do contato: ')# tem que ser cadastrado por algo unico como um cpf ou email
        if not contatos_Existentes(pasta, email):
            break
        else:
            print('Esse e-mail já está cadastrado.')
            print('Por favor, tente com outro e-mail.')
    #nesse passo, o email recebido será único

    contato = {#dicionario
        'nome': input('Digite seu nome: '),
        'email': email,
        'twitter': input('Digite o usuario do twitter: '),
        'telefone': input('Digite o telefone do contato: '),
        'instagram': input('Digite usuario do instagram: ')
    }
    pasta.append(contato)
    print('O contato {} foi cadastrado!\n'.format(contato['email']))


def alterar(pasta):# bloco de função para alterar contatos cadastrados
    if len(pasta)>0:

        email = input('Digite o e-mail do contato a ser alterado: ')
        print('-='*24)

        if contatos_Existentes(pasta, email):
            for i, contato in enumerate(pasta):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Twitter: {}'.format(contato['twitter']))
                    print('Email: {}.'.format(contato['email']))
                    print('Telefone: {}.'.format(contato['telefone']))
                    print('Instagram: {}.'.format(contato['instagram']))
                    print('-='*24) 

                    contato['nome'] = input('Digite novo nome de usuario : ')
                    contato['twitter'] = input('Digite novo usuario do twitter: ')
                    contato['instagram'] = input('Digite novo usuario do instagram: ')
                    contato['telefone'] = input('Digite o novo telefone  do contato: ')
                    print('Os dados do contato com o e-mail {}, foram alterados com sucesso!'.format(contato['email']))
                    break
        else:
            print('Não existe contato cadastrado com o email {}.'.format(email))     
    else:
        print('Não existem contatos cadastrados.\n')

def excluir(pasta):# bloco de função para excluir um contato registrado
    if len(pasta)>0:

        email = input('Digite o e-mail do contato a ser excluído: ')
        print('-='*24)
        if contatos_Existentes(pasta, email):
            for i, contato in enumerate(pasta):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Twitter: {}'.format(contato['twitter']))
                    print('Email: {}.'.format(contato['email']))
                    print('Telefone: {}.'.format(contato['telefone']))
                    print('Instagram: {}.'.format(contato['instagram']))
                    print('-='*24) 

                    del pasta[i]
                    print('O contato foi apagado com sucesso!')
                    break
        else:
            print('Não existe contato cadastrado com o email {}.\n'.format(email))     
    else:
        print('Não existem contatos cadastrados.\n')

def buscar(pasta):# bloco de função para buscar por um email registrado
    if len(pasta)>0:

        email = input('Digite o e-mail do contato a ser encontrado: ')
        print('-='*24)
        if contatos_Existentes(pasta, email):
            for i, contato in enumerate(pasta):
                if contato['email'] == email:
                    print('Nome: {}'.format(contato['nome']))
                    print('Twitter: {}'.format(contato['twitter']))
                    print('Email: {}.'.format(contato['email']))
                    print('Telefone: {}.'.format(contato['telefone']))
                    print('Instagram: {}'.format(contato['instagram']))
                    print('-='*24)
                    break 
        else:
            print('Não existe contato cadastrado com o email {}.'.format(email))     
    else:
        print('Não existem contatos cadastrados.\n')

def listar(pasta):# bloco de função para listar todos os contatos registrados
    if len(pasta)>0:
        for i, contato in enumerate(pasta):
            print('Contato {}:'.format(i+1))

            print('\tNome: {}'.format(contato['nome']))
            print('\tTwitter: {}'.format(contato['twitter']))
            print('\tEmail: {}.'.format(contato['email']))
            print('\tTelefone: {}.'.format(contato['telefone']))
            print('\tInstagram: {}'.format(contato['instagram']))
            print('-='*24)

    else:
        print('Não existem contatos cadastrados.')

def principal():# menu

    pasta = carregar_Contatos() # aqui inicia a pasta