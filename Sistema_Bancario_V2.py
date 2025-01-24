from datetime import datetime, timezone

menu = """
=====================================
    Selecione a opção desejada:


[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


=====================================
"""

saldo = 0
valor_limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
numero_transacoes = 0
LIMITE_TRANSACOES = 10
data_ultimo_reset = datetime.now(timezone.utc).date()

def obter_data_formatada():
    """Obtém a data e hora atual formatada."""
    return datetime.now(timezone.utc).strftime("%A, %d. %B %Y %I:%M%p")

def exibir_menu():
    """Exibe o menu de opções."""
    print(menu)

def reset_limites_diarios (numero_saques, numero_transacoes, data_ultimo_reset):
 #      '''Verifica se o dia mudou para resetar os contadores limites.'''
    hoje = datetime.now(timezone.utc).date()
    if hoje != data_ultimo_reset:
        numero_saques = 0
        numero_transacoes = 0
        data_ultimo_reset = hoje

    return data_ultimo_reset, numero_saques, numero_transacoes

def realizar_deposito(saldo, extrato, numero_transacoes):
    '''Realiza um depósito na conta, adicionando o valor ao saldo e registrando a transação no extrato.
       Atualiza o número de transações realizadas no dia.'''
    try:
        valor = float(input("Informe o valor do depósito: "))

        execedeu_transacoes = numero_transacoes >= LIMITE_TRANSACOES

        if execedeu_transacoes:
            print("Operação falhou! Você excedeu o numero de transações diárias.")
        
        elif valor > 0:
            saldo += valor
            data_transacao = obter_data_formatada()
            extrato.append(f"Deposito: R$ {valor:.2f}       {data_transacao}\n")
            numero_transacoes += 1
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.\n")    
        else:
            print ("Operação falhou! O valor informado é invalido.")
    except ValueError:
        print("Falha no Depósito. Por favor, insira um valor numérico.")

    return saldo, extrato, numero_transacoes

def realizar_saque(saldo, extrato, numero_saques, numero_transacoes):
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
            data_transacao = obter_data_formatada()
            extrato.append(f"Saque: R$ {valor:.2f}      {data_transacao}\n")
            numero_saques += 1
            numero_transacoes += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
        else:
            print("Operação falhou! O valor informado é invalido.") 

    except ValueError:
        print("Falha no Saque. Por favor, ensira um valor numérico.")

    return saldo, extrato, numero_saques, numero_transacoes

def exibir_extrato (saldo, extrato, obter_data_formatada):
    '''Exibe o extrato e todas as movimentações realizadas com data e hora de cada uma.'''
    print("\n===============EXTRATO===============")
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        for linha in extrato:
            print(linha)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================")
    print(obter_data_formatada)

def processar_opcao(opcao, saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset):
    """Processa a opção escolhida pelo usuário."""
    continuar = True  # Define o valor padrão como True
    if opcao == "1":
        saldo, extrato, numero_transacoes = realizar_deposito(saldo, extrato, numero_transacoes)
    elif opcao == "2":
        saldo, extrato, numero_saques, numero_transacoes = realizar_saque(saldo, extrato, numero_saques, numero_transacoes)
    elif opcao == "3":
        exibir_extrato(saldo, extrato, obter_data_formatada())
    elif opcao == "0":
        print("Muito obrigado por utilizar nossos serviços!")
        continuar = False  # Define para False ao sair
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")

    return saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset, continuar

while True:
#   '''Loop principal, onde o menu é exibido e há a interação com o usuário.'''
    data_ultimo_reset, numero_saques, numero_transacoes = reset_limites_diarios(data_ultimo_reset, numero_saques, numero_transacoes)
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset, continuar = processar_opcao( opcao, saldo, extrato, numero_saques, numero_transacoes, data_ultimo_reset)

    if not continuar:
        break
