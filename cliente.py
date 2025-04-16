from priorityQueue import priorityQueue

def menu():
    print("-----------------------------------------------------")
    print("1. Chegada de pessoa para atendimento")
    print("2. Atendimento de uma pessoa")
    print("3. Listar todas as pessoas da fila")
    print("4.  Gerar informações sobre os atendimentos realizados e o tamanho atual da fila")
    print("5. SAIR")
    

fila = priorityQueue()
atendimentos_normais = 0
atendimentos_prioridade = 0

while True:

    menu()
    op = input("Selecione a opção desejada: ")

    if (op == '1'):
        print("-----------------------------------------------------")
        print("ATENDIMENTO:")
        print("1 - Prioridade")
        print("2 - Normal")

        modalidade = input("Selecione a modalidade do atendimento: ")

        if (modalidade == '1'):
            nome = input("Nome da pessoa: ")
            #queue.enqueue(nome, True)
            print(f"Pronto. A pessoa '{nome}' foi adicionada na fila na modalidade PRIORIDADE")
            
        elif (modalidade == '2'):
            nome = input("Nome da pessoa: ")
            #queue.dequeue(nome, False)
            print(f"Pronto. A pessoa '{nome}' foi adicionada na fila na modalidade NORMAL")
            
        else: 
            print("OPÇÃO INVÁLIDA! RETORNANDO AO MENU.")

    elif (op == '2'):
        print("-----------------------------------------------------")

    elif (op == '3'):
        print("-----------------------------------------------------")

    elif (op == '4'):
        print("-----------------------------------------------------")

    elif (op == '5'):
        print("-----------------------------------------------------")

    else:
        print("-----------------------------------------------------")
        print("OPÇÃO INVÁLIDA. RETORNANDO AO MENU. TENTE NOVAMENTE.")