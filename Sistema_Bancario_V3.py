from datetime import datetime, timezone

saldo = 0
valor_limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
numero_transacoes = 0
LIMITE_TRANSACOES = 10
data_ultimo_reset = datetime.now(timezone.utc).date()
conta = []
usuarios = []
usuario = []

def data_hora():
    """Obtém a data e hora atual formatada."""
    return datetime.now(timezone.utc).strftime("%A, %d. %B %Y %I:%M%p")

def exibir_menu():
    """Exibe o menu de opções."""
    menu = """
    =====================================
        Selecione a opção desejada:


    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [0] Sair


    =====================================
"""

    print(menu)

def reset_limites_diarios (numero_saques, numero_transacoes, data_ultimo_reset):
#      '''Verifica se o dia mudou para resetar os contadores limites.'''
    hoje = datetime.now(timezone.utc).date()
    if hoje != data_ultimo_reset:
        numero_saques = 0
        numero_transacoes = 0
        data_ultimo_reset = hoje

    return data_ultimo_reset, numero_saques, numero_transacoes

def depositar(saldo, extrato, numero_transacoes, /):
    '''Realiza um depósito na conta, adicionando o valor ao saldo e registrando a transação no extrato.
    Atualiza o número de transações realizadas no dia.'''
    try:
        valor = float(input("Informe o valor do depósito: "))

        execedeu_transacoes = numero_transacoes >= LIMITE_TRANSACOES

        if execedeu_transacoes:
            print("Operação falhou! Você excedeu o numero de transações diárias.")
        
        elif valor > 0:
            saldo += valor
            data_transacao = data_hora()
            extrato.append(f"Deposito: R$ {valor:.2f}       {data_transacao}\n")
            numero_transacoes += 1
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.\n")    
        else:
            print ("Operação falhou! O valor informado é invalido.")
    except ValueError:
        print("Falha no Depósito. Por favor, insira um valor numérico.")

    return saldo, extrato, numero_transacoes

def sacar(*, saldo, extrato, numero_saques, numero_transacoes):
#'''Realiza um saque na conta, removendo o valor ao saldo e registrando a transação no extrato.
#   Atualiza o número de transações realizadas no dia.
#   Limita o número de saques diários a 3'''
    try:
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > valor_limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        execedeu_transacoes = numero_transacoes >= LIMITE_TRANSACOES
        
        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor informado excedeu o limite.")
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o numero de saques diários.")
        elif execedeu_transacoes:
            print("Operação falhou! Você excedeu o numero de transações diárias.")
        elif valor>0:
            saldo -= valor
            data_transacao = data_hora()
            extrato.append(f"Saque: R$ {valor:.2f}      {data_transacao}\n")
            numero_saques += 1
            numero_transacoes += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
        else:
            print("Operação falhou! O valor informado é invalido.") 

    except ValueError:
        print("Falha no Saque. Por favor, ensira um valor numérico.")

    return saldo, extrato, numero_saques, numero_transacoes

def exibir_extrato (saldo, extrato, data_hora):
    '''Exibe o extrato e todas as movimentações realizadas com data e hora de cada uma.'''
    print("\n===============EXTRATO===============")
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================")
    print(data_hora)

def criar_usuario(usuarios, usuario):
    '''Cria um novo usuário e adiciona a lista de usuários.'''
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    usuario = {"nome": nome, "cpf": cpf, "contas": []}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    return usuario, usuarios

def criar_conta(conta, usuarios):
    '''Cria uma nova conta e adiciona a lista de contas de um usuário específico.'''
    nome = input("Informe o nome do titular da conta: ")
    cpf = input("Informe o CPF do titular da conta: ")
    
    # Procura o usuário pelo CPF
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:  # Comparando o CPF
            usuario = u
            break
    
    if usuario is None:
        print("Usuário não encontrado. Crie o usuário antes de criar a conta.")
        return conta, usuarios
    
    conta = [nome, cpf]  # Cria a conta
    if "contas" not in usuario:
        usuario.append({"contas": []})  # Se não houver uma lista de contas no usuário, cria uma
    usuario["contas"].append(conta)  # Adiciona a conta ao usuário
    
    print("Conta criada com sucesso!")
    return conta, usuarios

def processar_opcao(opcao, saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset, conta, usuario, usuarios):
    """Processa a opção escolhida pelo usuário."""
    continuar = True  # Define o valor padrão como True
    if opcao == "1":
        saldo, extrato, numero_transacoes = depositar(saldo, extrato, numero_transacoes)
    elif opcao == "2":
        saldo, extrato,numero_saques, numero_transacoes = sacar(
            saldo=saldo,
            extrato=extrato,
            numero_saques=numero_saques,
            numero_transacoes=numero_transacoes
            )
    elif opcao == "3":
        exibir_extrato(saldo, extrato, data_hora())
    
    elif opcao == "4":
        usuario, usuarios = criar_usuario(usuarios, usuario)
    
    elif opcao == "5":
        conta, usuarios = criar_conta(conta, usuarios)
    
    elif opcao == "0":
        print("Muito obrigado por utilizar nossos serviços!")
        continuar = False  # Define para False ao sair
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")

    return saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset, conta, usuario, usuarios, continuar

while True:
#   '''Loop principal, onde o menu é exibido e há a interação com o usuário.'''
    data_ultimo_reset, numero_saques, numero_transacoes = reset_limites_diarios(data_ultimo_reset, numero_saques, numero_transacoes)
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset, conta, usuario, usuarios, continuar = processar_opcao(opcao, saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset, conta, usuario, usuarios)

    if not continuar:
        break
