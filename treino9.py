saldo = 0

while True:
    print("\n===MENU do banco gc===")
    print("1. ver saldo")
    print("2. depositar")
    print("3. sacar")
    print("4. sair")

    opcao = input("escolha uma opçao:")

    if opcao == "1":
        print(f"seu saldo e de R${saldo:.2f}")

    elif opcao == "2":
        valor = float(input("digite um valor:"))
        saldo + valor
        print("deposito realizado")

    elif opcao == "3":
        valor = float(input("digite um valor de saque:"))
        if valor <= saldo:
            saldo -= valor
            print("saque realizado")
        else:
            print("saldo insuficiente")

    elif opcao == "4":
        print("saindo")
        break
else:
    Print("opcao invalida")                        