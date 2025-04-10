contatos = []


while True:
    print("\n1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Remover contato")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ") # variavel recebe o nome
        telefone = input("Digite o telefone: ") #variavel recebe telefone
        
        contatos[nome] = telefone  # Adiciona nome e telefone dentro de contatos
        print(f"Contato {nome} adicionado!")

    elif opcao == "2":
        if len(contatos) == 0:
            print("Nenhum contato salvo.")
        else:
            print("\nLista de Contatos:")
            for nome, telefone in contatos.items():
                print(f"{nome} - {telefone}")

    elif opcao == "3":
        nome = input("Digite o nome do contato a remover: ")
        
        if nome in contatos:
            del contatos[nome]  # Remove o contato
            print(f"Contato {nome} removido!")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        print("Saindo...")
        break  # Sai do loop

    else:
        print("Opção inválida! Tente novamente.")
