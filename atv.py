tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas

def adicionar_tarefa(tarefa): # def indica que uma funçao será definida
    tarefas.append(tarefa)    # .append serve para adicionar tarefas a cada uma das listas
    historico.append(tarefa)
    fila_execucao.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada!\n") 

def desfazer_ultima_tarefa(): 
    if historico:
        ultima = historico.pop()
        tarefas.remove(ultima)
        fila_execucao.remove(ultima)
        print(f"Tarefa '{ultima}' desfeita!\n")
    else:
        print("Nenhuma tarefa para desfazer.\n")

def atender_tarefa():
    if fila_execucao:
        feita = fila_execucao.pop(0)
        tarefas.remove(feita)
        print(f"Tarefa '{feita}' atendida!\n")
    else:
        print("Nenhuma tarefa para atender.\n")

def mostrar_tarefas():
    print("\n📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas):
        print(f"{i + 1}. {t}")
    print()

while True:
    print("1. Adicionar Tarefa")
    print("2. Desfazer Última Tarefa")
    print("3. Atender Tarefa (modo fila)")
    print("4. Mostrar Tarefas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == '2':
        desfazer_ultima_tarefa()
    elif opcao == '3':
        atender_tarefa()
    elif opcao == '4':
        mostrar_tarefas()
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!\n")