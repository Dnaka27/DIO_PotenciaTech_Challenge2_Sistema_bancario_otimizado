# Constantes
LIMITE_SAQUE_DIARIO = 3
AGENCIA_PADRAO = "0001"
LIMITE_SAQUE = 500

# Funções principais

def iniciar():
    print(f"""
{'=' * 30}
{'Seja bem-vindo'.center(30)}
{'-' * 30}""")
    exibir_menu()

def exibir_menu():
    saldo = 0
    qtd_saques = 0
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = input("""\nOpções:
        1. Depositar
        2. Sacar
        3. Extrato
        4. Saldo
        5. Criar Conta
        6. Listar Contas
        7. Criar Usuário
        0. Encerrar sessão
        Escolha uma opção: """).strip()

        if opcao in ("1", "a", "A"):
            saldo, extrato = depositar(saldo, extrato)
        elif opcao in ("2", "b", "B"):
            saldo, extrato, qtd_saques = sacar(saldo, extrato, qtd_saques)
        elif opcao in ("3", "c", "C"):
            mostrar_extrato(saldo, extrato)
        elif opcao in ("4", "d", "D"):
            mostrar_saldo(saldo)
        elif opcao in ("5", "e", "E"):
            criar_conta(usuarios, contas)
        elif opcao in ("6", "f", "F"):
            listar_contas(contas)
        elif opcao in ("7", "g", "G"):
            criar_usuario(usuarios)
        elif opcao in ("0", "z", "Z"):
            encerrar_sessao()
            break
        else:
            print("Opção inválida! Tente novamente.")

def depositar(saldo, extrato):
    valor = float(input("Valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito de: R${valor:.2f}"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito!")
    return saldo, extrato

def sacar(saldo, extrato, qtd_saques):
    if qtd_saques >= LIMITE_SAQUE_DIARIO:
        print("Limite de saques diários excedido!")
        return saldo, extrato, qtd_saques

    valor = float(input("Valor do saque: "))
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > LIMITE_SAQUE:
        print(f"Saque excede o limite de R${LIMITE_SAQUE}!")
    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque de: R${valor:.2f}"
        qtd_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor inválido para saque!")
    return saldo, extrato, qtd_saques

def mostrar_extrato(saldo, extrato):
    print("\n=== Extrato ===")
    print(extrato if extrato else "Extrato vazio.")
    print(f"\nSaldo: R${saldo:.2f}")
    print("=" * 30)

def mostrar_saldo(saldo):
    print("\n=== Saldo ===")
    print(f"Saldo: R${saldo:.2f}")
    print("=" * 30)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (Rua, Número, Bairro, Cidade/Estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta(usuarios, contas):
    cpf = input("Informe o CPF do titular: ")
    usuario = next((user for user in usuarios if user['cpf'] == cpf), None)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"agencia": AGENCIA_PADRAO, "numero_conta": numero_conta, "titular": usuario['nome']})
        print(f"Conta {numero_conta} criada para {usuario['nome']}!")
    else:
        print("Usuário não encontrado!")

def listar_contas(contas):
    print("\n=== Contas ===")
    if not contas:
        print("Nenhuma conta cadastrada.")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['titular']}")
    print("=" * 30)

def encerrar_sessao():
    print("Sessão encerrada. Obrigado!")

# Executar programa
iniciar()
