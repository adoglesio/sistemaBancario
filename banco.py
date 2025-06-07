saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

while True:
    print("""
====== MENU ======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
==================
    """)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido! Informe um valor positivo.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        if numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("Limite diário de saques atingido.")
        elif valor > limite_saque:
            print("Valor do saque excede o limite de R$ 500.00.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido! Informe um valor positivo.")

    elif opcao == "3":
        print("\n====== EXTRATO ======")
        if extrato:
            print(extrato.strip())
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("======================")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")
