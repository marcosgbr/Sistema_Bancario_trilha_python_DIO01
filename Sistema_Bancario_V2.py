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
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_transacoes = 0
LIMITE_TRANSACOES = 10

hoje = datetime.now(timezone.utc )
data_formatada = hoje.strftime("%A, %d. %B %Y %I:%M%p")

def exibir_menu():
    print(menu)

def realizar_deposito(saldo, extrato, numero_transacoes):
    try:
        valor = float(input("Informe o valor do depósito: "))

        execedeu_transacoes = numero_transacoes >= LIMITE_TRANSACOES

        if execedeu_transacoes:
            print("Operação falhou! Você excedeu o numero de transações diárias.")
        
        elif valor > 0:
            saldo += valor
            data_transacao = datetime.now(timezone.utc)
            data_transacao_formatada = data_transacao.strftime("%A, %d. %B %Y %I:%M%p")
            extrato += f"Deposito: R$ {valor:.2f}       {data_transacao_formatada}\n"
            numero_transacoes += 1
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.\n")    
        else:
            print ("Operação falhou! O valor informado é invalido.")
    except:
        print("Falha no Depósito. Por favor, ensira um valor numérico.")

    return saldo, extrato, numero_transacoes,


def realizar_saque(saldo, extrato, numero_saques, numero_transacoes):
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
            data_transacao = datetime.now(timezone.utc)
            data_transacao_formatada = data_transacao.strftime("%A, %d. %B %Y %I:%M%p")
            extrato += f"Saque: R$ {valor:.2f}      {data_transacao_formatada}\n"
            numero_saques += 1
            numero_transacoes += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.\n")
        
        else:
            print("Operação falhou! O valor informado é invalido.") 

    except:
        print("Falha no Saque. Por favor, ensira um valor numérico.")

    return saldo, extrato, numero_saques, numero_transacoes

def exibir_extrato (saldo, extrato, data_formatada):
    print("\n===============EXTRATO===============")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================")
    print(data_formatada)
    return (" ")
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        saldo, extrato, numero_transacoes = realizar_deposito(saldo, extrato, numero_transacoes)
    
    elif opcao == "2":
        saldo, extrato, numero_saques, numero_transacoes = realizar_saque(saldo, extrato, numero_saques, numero_transacoes)
            
    elif opcao == "3":
        exibir_extrato(saldo, extrato, data_formatada)
    
    elif opcao == "0":
        print("Muito obrigado por utilizar nossos serviços!")

        break
    else:
        print("Opção inválida! Por favor, selecione uma opção válida.")
