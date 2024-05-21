from time import sleep

menu = """
####### Menu #######
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
#Variavel que armazena o saldo
saldo = 1000
#Variavel que armazena valor limite do saque
limit = 500
#Contador do número de saco
numero_de_saques = 1
#Constante do limite máximo de saque.
LIMITE_SAQUES = 3
#Variavel que acumula as Strings do extrato
extrato = ""

#variavel para regra de seleção de menu
opcao = 0
#Repetidor para interação com usuário
while (opcao >= 0) and (opcao <= 4):
    #varivavel de interação
    opcao = int(input(menu))
    #opcao que retorna para o menu
    
    if opcao == 0:
        print(menu)
        
    #opcao de deposito de dinheiro 
    elif opcao == 1:
        print("Abrindo Deposito...")
        sleep(1)
        print(" Deposito ".center(20, '#'))
        deposito = float(input("Informe o valor do deposito: "))
        #regra para validar depositor maior que zero
        if deposito > 0:
            saldo += deposito
            print(f"Valor depositado de + {deposito}")
            extrato += str(f"Valor depositado de: + {deposito} \n")
            print("Retornando ao menu...")
            sleep(1)
        #caso o deposito seja inferior a 0, cai nessa regra e retorna ao menu
        else:
            print("Operação falhou.")
            print("Retornando ao menu...")
            sleep(1)
            opcao = 0
                            
    #opcao de sacar dinheiro            
    elif opcao == 2:
        print("Abrindo Sacar...")
        sleep(1)
        print(" Sacar ".center(20, '#'))
        saque = float(input("Qual valor deseja sacar: "))
        #Regra para validar a quandiade de saque diário
        if numero_de_saques <= LIMITE_SAQUES:
            numero_de_saques += 1
            #regra para validar se o saque é maior que 500R$
            if saque > 500:
                    print("Saque maior que o limite")
                    print("Retornando ao menu...")
                    sleep(1)
            #regra para validar se possui saldo disponivél para saque
            elif saque <= saldo:
                saldo -= saque
                print(f"Valor sacado de - {saque}")
                extrato += str(f"Saque realizado de: - {saque}\n")
                print("Retornando ao menu...")
                sleep(1)
            #retorno em caso de saldo insuficiente     
            else:
                print("Operação falhou. Saldo insuficiente.")
                print("Retornando ao menu...")
                sleep(1)
                opcao = 0
        #retorno de limite diário atingido
        else:
            print("Limite de saque atingido.")
            print("Retornando ao menu...")
            sleep(1)
            opcao = 0
        
    #Opcao para printar extrato na tela    
    elif opcao == 3:
        print("Abrindo Extrato...")
        print(" Extrato ".center(20, '#'))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(20, '-'))
        
        print("\n Retornando ao menu...")
        sleep(1)
     
    #Opcao para sair do aplicativo    
    elif opcao == 4:
        print(" Saindo ".center(20, '#'))
        sleep(2)
        exit()
        
    #Regra para tratamento caso usuáro digite algum valor não permitido de opção    
    else:
        print("Opção inválida! Digite um opção correta.")
        print("Abrindo menu...")
        sleep(2)
        opcao = 0





