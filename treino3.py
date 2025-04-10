tarefas = []  # Lista para armazenar tarefas

while True:
    print("\n1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif escolha == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa adicionada.")
        else:
            print("\nSuas tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    elif escolha == "3":
        print("Saindo...")
        break  # Sai do loop e encerra o programa

    else:
        print("Opção inválida! Tente novamente.")
