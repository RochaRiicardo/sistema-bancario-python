import json

conta = []

# CARREGAR ARQUIVOS AO ABRIR PROGRAMA
def carregar_arquivo():
    try:
        with open("contas.json", "r", encoding="utf-8") as dados:
            dados_salvo = json.load(dados)
            return dados_salvo
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# SALVAR EM JSON
def salvar_arquivo():
    with open("contas.json", "w", encoding="utf-8") as dados:
        json.dump(conta, dados, ensure_ascii=False, indent=4)

# CADASTRAR CONTA
def cadastrar_conta():
    nome = input("Nome do Titular: ").lower().strip()
    sobrenome = input("Sobrenome: ").lower().strip() 
    
    for cadastro in conta:
        if cadastro["nome"] == nome:
            print("Esta pessoa ja possui conta")
            return
        
    cadastro = {
        "nome": nome,
        "sobrenome": sobrenome,
        "saldo": 0.0, 
        "historico": []
    }

    conta.append(cadastro)
    salvar_arquivo()
    print(f"Cadastrado {nome} {sobrenome} com sucesso! ")

# DEPOSITO EM CONTA 
def depositar():
    titular = input("Nome do titular para o depósito: ").lower().strip()
    
    for cadastro in conta:
        if cadastro["nome"] == titular:
            valor = float(input("Qual valor a depositar: "))
            cadastro["saldo"] += valor 
            cadastro["historico"].append(f"Deposito de R$ {valor:.2f}")
            salvar_arquivo()
            print("Depósito realizado com sucesso!")
            return
            
    print("Conta não encontrada!")

# SACAR
def sacar():
    titular = input("Nome do titular: ").lower().strip()
    saque = float(input("Qual valor do saque: "))
    
    for cadastro in conta:
        if cadastro["nome"] == titular:
            if saque <= cadastro["saldo"]: 
                cadastro["saldo"] -= saque 
                cadastro["historico"].append(f"Saque: R$ {saque:.2f}")
                salvar_arquivo()
                print("Saque realizado!")
                return
            else:
                print("Saldo insuficiente!")
                return
                
    print("Conta não encontrada!")

# TRANSFERÊNCIA ENTRE CONTAS
def transferencia():
    print("\n #### TRANSFERÊNCIA ENTRE CONTAS ####")

    origem = input("Nome da conta de transferência: ").lower().strip()
    destino = input("Nome da conta a receber o valor: ").lower().strip()
    valor = float(input("Qual valor deseja transferir: "))

    ### VARIÁVEIS TEMPORÁRIAS ATÉ ENCONTRAR AS CONTAS
    conta_origem = None
    conta_destino = None

    for cadastro in conta:
        if cadastro["nome"] == origem:
            conta_origem = cadastro
        if cadastro["nome"] == destino:
            conta_destino = cadastro
    
    # VALIDAÇÃO DE SEGURANÇA
    if conta_origem is None:
        print("A Sua conta não foi encontrada")
        return
    
    if conta_destino is None:
        print("A conta de destino nao foi encontrada")
        return
    
    if valor > conta_origem["saldo"]:
        print("Saldo insuficiente para transferência")
        return
    
    # PROCESSAMENTO DA TRANSFERÊNCIA SE PASSAR NO CHECK
    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor

    # ATUALIZA O HISTÓRICO DAS CONTAS
    conta_origem["historico"].append(f"Transferência enviada para {destino}: R$ {valor:.2f}")
    conta_destino["historico"].append(f"Transferência recebida de {origem}: R$ {valor:.2f}")

    salvar_arquivo()
    print(f"Transferência de R$ {valor:.2f} realizada com sucesso para {destino}!")

# HISTÓRICO
def historico_de_movimentacoes():
    print("\n #### MOVIMENTAÇÕES ###")
    titular = input("Digite o nome do titular: ").lower().strip()

    for cadastro in conta:
        if cadastro["nome"] == titular:
            if len(cadastro["historico"]) == 0:
                print("Nenhuma movimentação")
            else:
                for operacao in cadastro["historico"]:
                    print(operacao)
            return
            
    print("Conta não encontrada")

# CONSULTAR SALDO
def consultar_saldo():
    titular = input("Nome do titular: ").lower().strip()

    for cadastro in conta:
        if cadastro["nome"] == titular:
            print(f"Seu saldo é: R$ {cadastro['saldo']:.2f}")
            return
            
    print("Conta não encontrada!")

# --- FLUXO PRINCIPAL DO PROGRAMA ---

conta = carregar_arquivo()

while True:
    print("\n #### MENU BANCO ###")
    print("1 - Cadastrar")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Consultar Saldo")
    print("5 - Transferência entre contas")
    print("6 - Movimentações")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_conta()

    elif opcao == "2": 
        sacar()

    elif opcao == "3":
        depositar()

    elif opcao == "4":
        consultar_saldo()

    elif opcao == "5":
        transferencia()

    elif opcao == "6":
        historico_de_movimentacoes()

    elif opcao == "7":
        salvar_arquivo()
        print("Saindo...")
        break
        
    else:
        print("Escolha uma opção válida")