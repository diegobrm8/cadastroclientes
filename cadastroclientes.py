clientes = []


def cadastro():
    while True:
        print('[Forneça as informações do usuário!]')
        dados = {}
        dados['NomeComp'] = input('Nome: ')
        dados['senha'] = input('Senha: ')
        dados['email'] = input('E-mail: ')
        dados['telefone'] = input('Telefone: ')
        dados['endereco'] = input('Endereço: ')

        # Verificar se o e-mail já existe na lista de clientes
        if any(cliente['email'] == dados['email'] for cliente in clientes):
            print('Este e-mail já está cadastrado. Tente novamente.')
            continue

        clientes.append(dados)
        print('Usuário cadastrado com sucesso!')

        # Solicitar login após o cadastro
        login = input('Deseja fazer login agora? (s/n): ')
        if login.lower() == 's':
            realizar_login(dados['email'])
            return
        elif login.lower() == 'n':
            break
        else:
            print('Opção inválida. Tente novamente.')


def realizar_login(email):
    while True:
        print('[Faça o login!]')
        email_login = input('E-mail: ')
        senha_login = input('Senha: ')

        for cliente in clientes:
            if cliente['email'] == email_login and cliente['senha'] == senha_login:
                print('Login bem-sucedido!')
                return
        print('E-mail ou senha incorretos. Tente novamente.')


def mostrarDados():
    email_cliente = input("Digite o e-mail do cliente para mostrar os dados: ")
    for cliente in clientes:
        if cliente['email'] == email_cliente:
            print("Nome:", cliente['NomeComp'])
            print("E-mail:", cliente['email'])
            print("Telefone:", cliente['telefone'])
            print("Endereço:", cliente['endereco'])
            return
    print("Cliente não encontrado.")


def mostrarClientes():
    if clientes:
        print("Clientes cadastrados:")
        for cliente in clientes:
            print("Nome:", cliente['NomeComp'])
            print("E-mail:", cliente['email'])
            print("Telefone:", cliente['telefone'])
            print("Endereço:", cliente['endereco'])
            print()  # Linha em branco para separar os clientes
    else:
        print("Não há clientes cadastrados.")


def menu():
    while True:
        print("\n0. Sair do programa")
        print("1. Cadastrar usuário")
        print("2. Mostrar dados de um cliente")
        print("3. Mostrar todos os clientes")
        print("4. Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 0:
                print('Encerrando o programa')
                return

            elif opcao == 1:
                cadastro()
            elif opcao == 2:
                mostrarDados()
            elif opcao == 3:
                mostrarClientes()
            elif opcao == 4:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
    

menu()

