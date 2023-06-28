# Funções

def iniciar():
    print(f"""
{'=' * 30}
{'Seja bem vindo'.center(30)}
{'-' * 30}""")
    menu()
    
def menu():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    qtd_saques = 0
    limite = 500
    extrato = ""
    usuarios = []
    contas = []

    while True:
        print("""
Opções:

(1 / a). Depositar
(2 / b). Sacar 
(3 / c). Gerar extrato
(4 / d). Ver saldo
(5 / e). Criar conta
(6 / f). Listar contas
(7 / g). Criar usuario

(0 / z). Encerrar sessao

------------------------------""")
        opcao = str(input("Resposta: ")).upper()
        if opcao == "1" or opcao == "A":
            valor = float(input("\nValor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2" or opcao == "B":
            if qtd_saques == 2:
                print(f"\n{'! Ultimo saque diario !'.center(30)}")
            valor = 0
            saldo, extrato, qtd_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, qtd_saques=qtd_saques, limite_saques=LIMITE_SAQUE)
        elif opcao == "3" or opcao == "C":
            mostrar_extrato(saldo, extrato=extrato)
        elif opcao == "4" or opcao == "D":
            verSaldo(saldo)
        elif opcao == "5" or opcao == "E":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "6" or opcao == "F":
            listar_contas(contas)
        elif opcao == "7" or opcao == "G":
            criar_usuario(usuarios)
        elif opcao == "0" or opcao == "Z":
            encerrar_sessao()
            break

def depositar(saldo, valor, extrato, /):
    print(f"\n{'-|- Deposito -|-'.center(30)}")
    if valor > 0:
        saldo += valor
        print("\n" + "- Deposito realizado -".center(30))
        extrato += f"\nDeposito de: {valor}"
    else:
        print("! Valor invalido !" .center(30))
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, qtd_saques, limite_saques):
    print(f"\n{'-|- Saque -|-'.center(30)}")
    if qtd_saques < limite_saques:
        valor = float(input("\nValor do saque: "))
        valor_excedido = valor > saldo
        limite_excedido = valor > limite
        if valor_excedido:
            print("! Valor maior que saldo !".center(30))
        elif limite_excedido:
            print("! Valor maior que limite !".center(30))
        elif valor > 0:
            saldo -= valor
            print("\n" + "- Saque realizado -".center(30))
            extrato += f"\nSaque de: {valor}"
            qtd_saques += 1
        else:
            print("! Valor invalido !" .center(30))
    else:
        print("! Limite de saques excedido !".center(30)) 

    return saldo, extrato, qtd_saques

def mostrar_extrato(saldo, /, *, extrato):
    print(f"\n{'-|- Extrato -|-'.center(30)}")
    if extrato == "":
        print(f"\n{'(Extrato limpo/vazio)'.center(30)}")
        print(f"\nSaldo de: {saldo}")
    else:    
        print(extrato)
        print(f"\n- Saldo de: {saldo}")
        print("-" * 30)

def verSaldo(saldo):
    print(f"\n{'-|- Saldo -|-'.center(30)}")
    print(f"\nSaldo: {saldo}")
    print("\n" + "-" * 30)

def criar_usuario(usuarios):
    print(f"\n{'-|- Criar usuario -|-'.center(30)}")
    cpf = input("\n - Informe o CPF (somente numeros): ")
    usuario = buscar_usuario(cpf, usuarios)
    
    if usuario:
        print(f"\n{'! CPF ja cadastrado !'.center(30)}")
        return None
    nome = input(" - Informe o nome completo: ")
    data_nascimento = input(" - Informe a data_nascimento(dd/mm/aaaa): ")
    print(" - Informe o endereco: ")
    rua = input("\nLogradouro/rua: ")
    numero_rua = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Sigla do estado: ")

    endereco = f"{rua}, {numero_rua} - {bairro} - {cidade}/{estado}"

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"\n{'- Usario criado com sucesso! -'.center(30)}")

def buscar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            usuario_buscado = usuario["nome"]
            return usuario_buscado
    return None

def criar_conta(agencia, numero_conta, usuarios):
    print(f"\n{'-|- Criar conta -|-'.center(30)}")
    cpf = input("\n - Informe o CPF (somente numeros): ")
    usuario = buscar_usuario(cpf, usuarios)

    if usuario:
        print(f"\n{' - Conta criada com sucesso! -'.center(30)}")
        info = input("\nDeseja ver informações da conta? (S = Sim / N = Não): ").upper()
        if info == "S":
            print(f"\n Agência: {agencia}\n Numero da conta: {numero_conta}")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print(f"\n{'! Usuario nao encontrado !'.center(30)}")
    print("\n(Opções => Criar usuario)")

def listar_contas(contas):
    print(f"\n{'-|- Buscar contas -|-'.center(30)}")
    for conta in contas:
        lista_contas = f"""
Agência:         {conta['agencia']}
Numero da conta: {conta['numero_conta']}
Titular:         {conta['usuario']}
        """
        print(lista_contas)

def encerrar_sessao():
    print(f"\n{'Sessao encerrada'.center(30)}")
    print("=" * 30)

# Executar

iniciar()