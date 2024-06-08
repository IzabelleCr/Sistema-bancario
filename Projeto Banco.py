import textwrap

def menu():
    menu = """
    ==================Menu=================
    [1] Depositar
    [2] Sacar
    [3] Visualizar Extrato
    [4] Cadastrar Usuário
    [5] Cadastrar Conta Bancária
    [6] Listar Contas Bancárias
    [0] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:  
        saldo += valor
        extrato += f" \nDepósito: R${valor:.2f}"
        print("Depósito realizado com SUCESSO!")
    else:
        print("Não foi possível realizar seu depósito.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite 
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("A Operação Falhou!! Você não tem saldo suficiente!")
    elif excedeu_limite:
        print("Operação Falhou!! O valor do saque é maior que o limite para sacar!")
    elif excedeu_saques:
        print("Operação falhou! Você excedeu o número de saques!")
    elif valor > 0:
        saldo -= valor
        extrato += f" \nSaque: R${valor:.2f}"
        numero_saques += 1
        print("=== Saque realizado com SUCESSO! ===")
    else: 
        print("Operação falhou! O valor informado é inválido!")
    return saldo, extrato

def visualizar_extrato(saldo, extrato):
    print('================ EXTRATO ================')
    print('Nenhuma movimentação foi realizada na conta' if not extrato else extrato)
    print(f'\n O Saldo na conta é de: R${saldo:.2f} Reais')
    print('==========================================')

def criar_usuario(usuarios):
    cpf = input("Digite o seu CPF (Apenas números!): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Um usuário já está registrado com esse CPF!")
        return
    
    nome = input("Informe seu nome Completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (rua, número, bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("--- Usuário cadastrado com sucesso! ---")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def verificar_conta_existente(cpf, contas):
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            return True
    return False

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado, fluxo de criação de conta encerrado!")
        return
    
    if verificar_conta_existente(cpf, contas):
        print("Este usuário já possui uma conta bancária!")
        return

    print("--- Conta criada com sucesso! ---")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "3":
            visualizar_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios, contas)
            if conta:
                contas.append(conta)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
