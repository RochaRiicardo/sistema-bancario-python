import json

livros = []


# CARREGAR ARQUIVOS AO ABRIR O PROGRAMA
def carregar_arquivo():
    try:
    
     with open(
        r"biblioteca.json",
        "r",
        encoding="utf-8"
    ) as arquivo:
        
        dados_biblioteca = json.load(arquivo)
        return dados_biblioteca
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    

# SALVAR EM JSON
def salvar_arquivo():
    with open(
        r"biblioteca.json",
        "w",
        encoding="utf-8"
    ) as arquivo:
        
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)
        



# CADASTRO DE LIVROS
def cadastrar_livro():
    nome = input("Nome do livro: ").lower().strip()
    autor = input("Nome do autor: ").lower().strip()
    for livro in livros:
        if livro["nome"] == nome:
            print("Esse livro ja esta cadastrado")
            return

    cadastro = {
        "nome": nome,
        "autor": autor,
        "status": "Disponivel"
    }

    livros.append(cadastro)
    salvar_arquivo()
    print(f"Livro {nome}, {autor} cadastrado")


# BUSCAR LIVRO
def buscar_livro():
    nome = input("Nome do livro para buscar: ").lower().strip()

    encontrou = False

    for livro in livros:
        if livro["nome"] == nome:
            print(f"{livro['nome']} ({livro['autor']}) - {livro['status']}")
            encontrou = True

    if not encontrou:
        print("Livro não existe na lista")


# EMPRESTAR O LIVRO
def emprestar_livro():
    nome = input("Nome do livro: ").lower().strip()

    for livro in livros:
        if livro["nome"] == nome:

            if livro["status"] == "Emprestado":
                print("Esse livro já está emprestado.")
                return

            livro["status"] = "Emprestado"
            salvar_arquivo()
            print("Livro emprestado")
            return

    print("Livro não encontrado")


# DEVOLVER LIVRO
def devolver_livro():
    nome = input("Nome do livro: ").lower().strip()

    for livro in livros:
        if livro["nome"] == nome:

            if livro["status"] == "Disponivel":
                print("Esse livro já está disponível.")
                return

            livro["status"] = "Disponivel"
            salvar_arquivo()
            print("Livro devolvido")
            return

    print("Livro não encontrado")


# MOSTRAR TODOS OS DADOS DE LIVROS
def mostrar_todos():
    print("\n### LISTA DE LIVROS ###")

    if len(livros) == 0:
        print("Nenhum livro cadastrado")
        return

    for livro in livros:
        print(f"- {livro['nome']} ({livro['autor']}) - {livro['status']}")


# MOSTRAR TODOS OS DISPONIVEIS
def mostrar_disponiveis():
    print("\n### LIVROS DISPONÍVEIS ###")

    encontrou = False

    for livro in livros:
        if livro["status"] == "Disponivel":
            print("-", livro["nome"])
            encontrou = True

    if not encontrou:
        print("Nenhum livro disponível")


# MOSTRAR TODOS EMPRESTADOS
def mostrar_emprestados():
    print("\n### LIVROS EMPRESTADOS ###")

    encontrou = False

    for livro in livros:
        if livro["status"] == "Emprestado":
            print("-", livro["nome"])
            encontrou = True

    if not encontrou:
        print("Nenhum livro emprestado")


# REMOVER LIVRO DA BIBLIOTECA
def remover_livro():
    nome = input("Nome do livro para remover: ").lower().strip()

    for livro in livros:
        if livro["nome"] == nome:
            livros.remove(livro)
            salvar_arquivo()
            print("Livro removido com sucesso")
            return

    print("Livro não encontrado")


def sair():
    print("Saindo...")

# CHAMANDO O CARREGAMENTO DE ARQUIVOS
livros = carregar_arquivo()

while True:

    print("\n### MENU ###")
    print("1 - Cadastrar Livro")
    print("2 - Emprestar Livro")
    print("3 - Buscar Livro")
    print("4 - Devolver Livro")
    print("5 - Mostrar Todos")
    print("6 - Mostrar Disponíveis")
    print("7 - Mostrar Emprestados")
    print("8 - Remover Livro")
    print("9 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        emprestar_livro()

    elif opcao == "3":
        buscar_livro()

    elif opcao == "4":
        devolver_livro()

    elif opcao == "5":
        mostrar_todos()

    elif opcao == "6":
        mostrar_disponiveis()

    elif opcao == "7":
        mostrar_emprestados()

    elif opcao == "8":
        remover_livro()

    elif opcao == "9":
        salvar_arquivo()
        sair()
        break

    else:
        print("Escolha uma opção válida.")












