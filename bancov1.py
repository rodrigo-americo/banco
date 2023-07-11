def sacar(*, valor, saldo, numero_saques, limite, extrato):
    LIMITE_SAQUE = 3
    if numero_saques < LIMITE_SAQUE:
        if verifica_valor(saldo, valor, limite):
            saldo -= valor
            extrato += f'Saque R$ {valor :.2f}\n '
            print(f'Valor {valor} sacado com sucesso. ')
            numero_saques += 1
            print(numero_saques)
    else:
        print("Desculpe mas já ecedu o limite de saques")

    return extrato, saldo, numero_saques


def verifica_valor(saldo, valor, limite):
    if valor > saldo:
        print('Saldo insuficiente')
    elif valor > limite:
        print("Tentativa de savar maior que o limite permitido")
    else:
        return True
    return False


def depositar(saldo, valor, extrato):
    if valor < 0:
        print('Desculpe mas não é possivel depositar valores negagito')
    else:
        print(f' valor {valor} depositado com sucesso.')
        saldo += valor
        extrato += f'Deposito R$ {valor:.2f}\n '
    return extrato, saldo


def imprimir_extrato(saldo, /, extrato):
    print('### Extrato ###')
    print('Não teve movimentação ' if not extrato else extrato)
    print(f'\n Saldo R${saldo:.2f}')


def cadastrar_cliente():
    cliente = {"Nome": "", "DataDeNacimento": "", "CPF": "", "Endereço": ""}
    cliente["Nome"] = input('Porfavor insira seu nome : ')
    cliente["DataDeNacimento"] = input('Porfavor informe sua data de nacimento :')
    cpf = input('Porfavor informe CPF : ')
    if valida_cpf(cpf):
        cliente["CPF"] = cpf
    else:
        print("Desculpe cpf já cadastrado")
        return
    cliente["Endereeço"] = input('Porfavor informe sue Endereço : ')

    clientes.append(cliente)


def valida_cpf(cpf):
    for i in range(len(clientes)):
        if clientes[i]["CPF"] == cpf:
            return False
    return cpf


def criar_conta_corrente():
    conta = {"Agencia": "001", "Numero": "", "Nome": ""}
    nome_cliente = input('Porfavor informe o nome do titular da conta')
    if validar_nome(nome_cliente):
        conta["Numero"] = "00" + str(len(conta)+1)
        conta["Nome"] = nome_cliente
        contas_correntes.append(conta)
    else:
        print("O nome digitado não é um de nossos cleintes")

    return


def validar_nome(nome_cliente):
    for i in range(len(clientes)):
        if clientes[i]["Nome"] == nome_cliente:
            return nome_cliente
    return False


menu = """
[0] Depositar
[1] sacar
[2] Extrato
[3] Cadastrar Cliente
[4] Criar Conta corrente
[5] Sair
=>"""

clientes = []
contas_correntes = []
saldo = 0.0
limite = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))

    if opcao == 0:
        valor = float(input('Digite o valor a depositar : '))
        extrato, saldo = depositar(saldo, valor, extrato)
    elif opcao == 1:
        valor = float(input('Digite o valor a sacar : '))
        extrato, saldo, numero_saques = sacar(valor=valor, saldo=saldo,
                                             limite=limite,
                                                numero_saques=numero_saques,
                                                extrato=extrato)
    elif opcao == 2:
        imprimir_extrato(saldo, extrato=extrato)

    elif opcao == 3:
        cadastrar_cliente()
    elif opcao == 4:
        cadastrar_cliente()
    else:
        print('Obrigado por usar nosso banco volte sempre')
        break
