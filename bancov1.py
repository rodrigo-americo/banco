menu = """

[0] Depositar
[1] sacar
[2] Extrato
[3] Sair

=>"""

saldo = 0.0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))

    if opcao == 0:
        valor = float(input('Digite o valor a depositar : '))
        if valor < 0:
            print('Não é possivel depositar valores negativos')
            continue
        else:
            print(f' valor {valor} depositado com sucesso.')
            saldo += valor
            extrato += f'Deposito R$ {valor:.2f}\n '
    elif opcao == 1:
        if numero_saques < LIMITE_SAQUE:
            valor = float(input('Digite o valor a sacar : '))
            if valor > limite and valor > saldo:
                print('Desculpe não é possivel sacar valores maior que R$ 500.00')
                continue
            else:
                saldo -= valor
                extrato += f'Saque R$ {valor :.2f}\n '
                print(f'Valor {valor} sacado com sucesso. ')
                numero_saques += 1
                print(numero_saques)
        else:
            print('Atingiu o numero maximo de saques ')
    elif opcao == 2:
        print('### Extrato ###')
        print('Não teve movimentação ' if not extrato else extrato)
        print(f'\n Saldo R${saldo:.2f}')
    else:
        print('Obrigado por usar nosso banco volte sempre')
        break
