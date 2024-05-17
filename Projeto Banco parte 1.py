## Projeto Banco parte 1 


menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUE = 3
numero_de_saques = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito=float(input("Quanto você gostaria de depositar ? :  " ))

        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito : R$ {deposito:.2f}\n '
            print('Depósito feito com sucesso!!')

        else:
            print('Ação Inválida! Impossível depositar saldo negativo.')
    
    elif opcao == '2':
        deposito = float(input('Qual valor você deseja sacar ? : '))

        excedeu_saldo = deposito > saldo

        excedeu_limite = deposito > limite

        excedeu_saques = numero_de_saques > LIMITE_SAQUE

        print(f'Saque de R$ {deposito:.2f} Reais foi feito! ')

        if excedeu_saldo:
            print('Ação falhou!! Você não tem saldo suficiente na conta!')

        elif excedeu_limite:
            print('Ação falhou! O Valor Excede o Limite do Banco! ')
        
        elif excedeu_saques:
            print('Ação Falhou!! O limite de saques diários foi atingido! ')

        elif deposito > 0: 
            saldo -= deposito
            extrato +=f'Saque: R$ {deposito:.2f}\n '
            numero_de_saques += 1


        else:
            print('Saque Falhou! O valor informado é inválido')

    elif opcao =='3':
        print('================EXTRATO================')
        print('Nenhuma movimentação foi realizada na conta' if not extrato else extrato)
        print('=======================================')
        print(f'\n O Saldo na conta é de: R$ {saldo:.2f} Reais')


    elif opcao == '4':
        print('Saindo do IzaBank, obrigada por utilizar')
        break

    else:
        print("Opção inválida, por favor selecione uma das opções")