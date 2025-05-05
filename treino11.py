import json
import os

ARQUIVOS = "arquivos.json"

def carregar_arquivos():
    if not os.path.exists(ARQUIVOS):
        return []
    with open(ARQUIVOS, 'r') as f:
        return json.load(f)
    
def salvar_arquivos(tarefas):
    with open(ARQUIVOS, 'w') as f:
        json.dump(tarefas, f, indent=4)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada")
    for t in tarefas:
        print(f"ID: {t['id']} | {t['titulo']} - {t['status']}")

def adicionar_tarefas(tarefas):
    titulo = input("digite o titulo:")
    descricao = input("digite a descriçao da tarefa:")
    nova = {
        "id": len(tarefas) + 1,
        "titulos": titulo,
        "descricao":descricao,
        "status": "pendente"
    }
    tarefas.append(nova)
    salvar_arquivos(tarefas)
    print("Tarefas adicionada!")

def atualizar_tarefas(tarefas):
    listar_tarefas(tarefas)
    id = int(input("digite o id da tarefa que deseja atualizar:"))
    for t in tarefas:
        if t["id"] == id:
            t["titulo"] = input("digite o novo titulo:")
            t["descricao"] = input("digite a nova descricao:")
            t["status"] = input("digite o novo status:")
            salvar_arquivos(tarefas)
            print("Tarefa atualizada!")
            return
    print("Tarefa não encontrada!")

def menu():
    tarefas = carregar_arquivos()
    while True:
        print("\n1. Listar tarfas")
        print("2. Adicionar tarefas")
        print("3. Atualizar tarefas") 
        print("0. sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefas(tarefas)
        elif opcao == "3":
            atualizar_tarefas(tarefas)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")