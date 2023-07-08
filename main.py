from datetime import datetime


def menu():
    print('''
*********** Bem-vindo ao nosso Banco ************

Digite um número referente ao serviço que deseja:

[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNovo Usuário
[5]\tListar Contas
[6]\tNova Conta
[7]\tSair

************************************************

''')

def sacar(*, saldo, valor, extrato, limite_dinheiro_saque, LIMITE_SAQUES, numero_saques):
    
    print('...::: Tela de Saque :::...')

    excedeuSaques = numero_saques >= LIMITE_SAQUES
    excedeuSaldo = valor > saldo
    excedeuLimite = valor > limite_dinheiro_saque

    if excedeuSaques:
        print('Você excedeu o número máximo de saques permitidos por dia!')

    elif excedeuLimite:
        print("Você excedeu o limite de Saque diário de R$ 500,00")

    elif excedeuSaldo:
            print('Saldo indisponível!')

    else:
        dataHora = obter_data_hora_atual()
        numero_saques += 1
        limite_dinheiro_saque -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f} - {dataHora} \n"
        print('Saque em processamento, por favor verifique a saída de dinheiro!')

    return saldo, extrato

def exibirExtrato(saldo, *, extrato, AGENCIA):
    extratoIndisponivel = saldo <= 0
    print(".........:::::::::::: EXTRATO ::::::::::::........")
    if extratoIndisponivel:
        print("    Não existe movimentações na conta atual!       ")

    else:
        print(extrato)
    print(":" * 50)
    
    return extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            dataHora = obter_data_hora_atual()
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f} - {dataHora}\n"
            print(f"\n=== Depósito realizado com sucesso! ===\n")
    else:
        print("\n=== Operação falhou! O valor informado é inválido. ===\n")
    
    return saldo, extrato


def obter_data_hora_atual():
    
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def criarUsuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("\n==== Usuário com CPF ja cadastrado no sistema! ====\n")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº, bairro - cidade/sigla estado): \n")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtro_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criarContaCorrente(agencia, numero_conta,usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtro_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n==== Usuário não encontrado, fluxo de criação de conta encerrado! ====")

def listar_contas(contas, /):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)


def main():
    
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite_dinheiro_saque = 500
    extrato = ""
    numero_saques = 0
    depositados = 0
    usuarios = []
    contas = []

    while True:
        
        menu()

        opcao = input()

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input("Informe o valor do saque: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_dinheiro_saque=limite_dinheiro_saque,
                LIMITE_SAQUES=LIMITE_SAQUES,
                numero_saques=numero_saques,
            )

        elif opcao == '3':
            exibirExtrato(
                saldo,
                extrato=extrato,
                AGENCIA=AGENCIA
                )
        
        elif opcao == '4':
            criarUsuario(usuarios)

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            numero_conta = len(contas) + 1
            conta = criarContaCorrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '7':
            print("Opção Sair selecionada. Até breve!")
            break

        else:
            print("Opção inválida! Digite um número de 1 a 7.")


main()

