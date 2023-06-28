menu = '''
*********** Bem-vindo ao nosso Banco ************

Digite um número referente ao serviço que deseja:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

************************************************

'''

saldo = 0
limite_dinheiro_saque = 500
extrato = 0
numero_saques = 0
depositados = 0
saque_aprovado = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print('Tela de Depósito')
        deposito = float(input('Digite o valor que deseja depositar: R$ '))
        saldo += deposito
        depositados += deposito
        print(f'Seu Saldo atual é R$ {saldo:.2f}')

        if deposito <= 0.0:
            print('''
            O deposito não pode ser realizado,
            por favor verifique a quantia que deseja depositar!''')

    elif opcao == "2":
        print('Tela de Saque')

        if numero_saques >= 3:
            print('Você excedeu o número máximo de saques permitidos por dia!')

        elif numero_saques < 3:
            print(f'''
            Você tem {LIMITES_SAQUES - numero_saques} saques disponíveis
            no valor de R$ {limite_dinheiro_saque:.2f} para hoje!''')
            valor_saque = float(input('Digite o valor desejado para sacar: R$ '))

            if saldo < valor_saque:
                print('Saldo indisponível!')

            elif saldo >= valor_saque:
                    saldo -= valor_saque
                    numero_saques += 1
                    saque_aprovado += valor_saque
                    limite_dinheiro_saque -= valor_saque
                    print('Saque em processamento, por favor verifique a saída de dinheiro!')

    elif opcao == "3":
        print('Tela de Extrato')

        if saldo <= 0:

            print('\n --- Não foram realizadas movimentações. ---')

        elif saldo > 0:
            print(f'''
            
            -----------------------------------------
                Extrato de transações
            
            Depositos efetuados - R$ {depositados}
            Valores sacados     - R$ {saque_aprovado}
            Saques efetuados    - {numero_saques}
            
            Limite saque diário - R$ {limite_dinheiro_saque}
            
            Saldo atual         - R$ {saldo:.2f}
            -----------------------------------------
        
            ''')

    elif opcao == "4":
        print('Até a próxima! É um prazer ter você como cliente! ;)')
        break

    else:
        print('''Operação inválida, por favor selecione novamente uma das
        opções existentes!''')