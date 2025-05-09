tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas
tarefas_execucao = []   # Tupla para armazenar a data e a prioridade das tarefas

# Função para salvar as tarefas no arquio "tarefas.txt"
def salvar_tarefas_txt():
    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:          # abertura do arquivo
        for tarefa, prioridade, data in tarefas_execucao:                # laço for percorre a tupla com todos os dados
            arquivo.write(f" '{tarefa}' ; '{prioridade}' ; '{data}' \n") # escreve cada tarefa no arquivo 

# Função para adicionar tarefas
def adicionar_tarefa(tarefa):                                          # 'def' indica que uma função será definida
    prioridade = input ("Digite a prioridade dessa tarefa: ")          # pede ao usuário que digite a prioridade da tarefa
    data = input ("Informe uma data para a tarefa ser executada: ")    # pede ao usuário que digite a data que deseja que a tarefa se realize
    tarefas_exec = (tarefa, prioridade, data)                          # criação de tupla com dados da tarefa
    tarefas_execucao.append(tarefas_exec)                              # adiciona a tupla na lista de tarefa
    salvar_tarefas_txt()                                               # chama a função para poder agir
    tarefas.append(tarefa)                                             # '.append' serve para adicionar tarefas a cada uma das listas
    historico.append(tarefa)                                           # adiciona uma tarefa à variável 'historico'
    fila_execucao.append(tarefa)                                       # adiciona uma tarefa na variável 'fila_execucao' 
    print(f"Tarefa '{tarefa}' '{prioridade}' '{data}' adicionadas!\n") # exibe uma mensagem para confirmar que a tarefa foi adicionada

# Função para desfazer a última tarefa adicionada
def desfazer_ultima_tarefa():
    if historico:                                # inicia uma condição para verificar se existe alguma tarefa no historico
        ultima = historico.pop()                 # remove a última tarefa adicionada (como uma pilha)
        tarefas.remove(ultima)                   # remove a tarefa da variável 'tarefas'
        fila_execucao.remove(ultima)             # remove a tarefa da 'fila_execucao' 
        print(f"Tarefa '{ultima}' desfeita!\n")  # exibe uma mensagem confirmando que a última tarefa foi desfeita
    else:                                        # caso a condição não for verdadeira
        print("Nenhuma tarefa para desfazer.\n") # exibe uma mensagem para mostrar que o 'historico' está vazio

# Função para atender a próxima tarefa da fila
def atender_tarefa():                            
    if fila_execucao:                           # inicia uma condição para verificar se a 'fila_execucao' tem alguma tarefa
        feita = fila_execucao.pop(0)            # remove a primeira tarefa da fila (como uma fila)
        tarefas.remove(feita)                   # remove a tarefa da variável 'tarefas'
        print(f"Tarefa '{feita}' atendida!\n")  # exibe a mensagem para confirmar que a tarefa foi executada
    else:                                       # caso a condição for falsa
        print("Nenhuma tarefa para atender.\n") # exibe uma mensagem para mostrar que a 'fila_execucao' está vazia

# Função para mostrar todas as tarefas
def mostrar_tarefas():
    print("\n📋 Lista de Tarefas:")                             # título da tarefa
    for i, t in enumerate(tarefas_execucao):                    # laço for para percorrer a lista de tarefas por índice 
        tarefa, prioridade, data = t                            # desempacota a tupla 
        print(f"{i + 1}. '{tarefa}' '{prioridade}' '{data}' ")  # exibe as tarefas por índice
    print()                                                     # linha em branco para espaçamento

# Inicia um loop (estrutura de repetição)
while True:
    # exibe cinco opções de tarefas
    print("1. Adicionar Tarefa")
    print("2. Desfazer Última Tarefa")
    print("3. Atender Tarefa (modo fila)")
    print("4. Mostrar Tarefas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")    # irá ler qual opção o usuário digitou

    if opcao == '1':                        # se a opção for igual a 1
        tarefa = input("Digite a tarefa: ") # pede a descrição da tarefa escolhida
        adicionar_tarefa(tarefa)            # chama a função para adicionar a devida tarefa
    elif opcao == '2':                      # se a opção for igual a 2
        desfazer_ultima_tarefa()            # chama a função para desfazer a última tarefa
    elif opcao == '3':                      # se a opção for igual a 3
        atender_tarefa()                    # chama a função para atender a tarefa
    elif opcao == '4':                      # se a opção for igual a 4
        mostrar_tarefas()                   # chama a função para mostrar a tarefa
    elif opcao == '5':                      # se a opção for igual a 5
        print("Saindo do programa...")      # exibe uma mensagem para sair do programa
        break                               # encerramento da estrutura de repetição
    else:                                   # caso alguma opção inexistente tenha sido escolhida
        print("Opção inválida!\n")          # uma mensagem será exibida para confirmar que a opção é inválida