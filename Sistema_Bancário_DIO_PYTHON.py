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

    
    
while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
    
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
    
        else:
            print ("Operação falhou! O valor informado é invalido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > valor_limite_saque
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor informado excedeu o limite.")
            
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o numero de saques diários.")
            
        elif valor>0:
        
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é invalido.") 
            
    elif opcao == "3":
        
        print("\n===========EXTRATO============")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")
    
    elif opcao == "0":
    
        print("Muito obrigado por utilizar nossos serviços!")
        break
