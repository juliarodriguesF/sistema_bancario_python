menu = """
Menu de Opções 
[a] - Depositar
[b] - Sacar 
[c] - Extrato
[d] - Sair 
"""
saldo = 0.0
valor = 0
extrato = ''
limite = 500
numeros_de_saque = 0

while True:
    opçao = input(menu)

    if opçao == "a":
        valor = float(input("Digite um valor a depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"foram depositados R${valor:.2f}\n"
            print(f"foram depositados R${
                  valor:.2f}, agora seu saldo é R${saldo:.2f}")
        else:
            print("Não foi possível efetuar o depósito")

    elif opçao == "b":
        valor = float(input("Digite um valor para sacar: "))
        if valor > saldo:
            print("Saldo insuficiente")
        elif valor > limite:
            print("O valor exede o limite")
        elif numeros_de_saque >= 3:
            print("exedeu o limite de operações de saque")
        elif valor > 0:
            saldo -= valor
            extrato += f"foram sacados R${valor:.2f}\n"
            print(f"foram sacados R${
                  valor:.2f}, agora seu saldo é R${saldo:.2f}")
            numeros_de_saque += 1
        else:
            print("Opção inválida ou não foi possível efetuar o saque")

    elif opçao == "c":
        print("EXTRATO BANCÁRIO")
        if not extrato:
            print("Nenhum histórico")
        else:
            print(extrato)
        print(f"Seu saldo é R${saldo:.2f}")

    elif opçao == "d":
        print("Saindo do Sistema, Obrigado!")
        break
    else:
        print("Opção inválida. Aperte qualquer tecla para escolher uma nova operação")
