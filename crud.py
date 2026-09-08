# CRUD em Python para realizar operações (create - read - update - delete).

# Cadastro de uma pessoa com dados básicos como (nome, idade, altura, cidade, endereço e cep).

# ====== Importações ======
import os

# Função para limpar o terminal assim que ela for chamada.
def clearTerminal():
    os.system("cls" if os.name == "nt" else "clear")

# Função para exibir o menu para o usuário.
def menu():
    print("\n1 - Cadastrar uma pessoa no sistema")
    print("2 - Exibir cadastros")
    print("3 - Atualizar dados de uma pessoa")
    print("4 - Excluir uma pessoa do sistema")
    print("5 - Sair do sistema")

# Funções do "CRUD"
def cadastrar(listaPessoas): # Criando uma pessoa...
    clearTerminal()
    print("\n====== CADASTRO DE PESSOAS ======")
    nome = input("\nDigite o seu nome completo: ")
    clearTerminal()

    try:
        idade = int(input("\nQuantos anos você tem? "))
        clearTerminal()
        altura = int(input("\nQual é a sua altura em centimetros: "))
        clearTerminal()
    except ValueError:
        clearTerminal()
        print("\nOpção inválida - Só aceito números!")
        input("\nPressione a tela ENTER continuar...")
        clearTerminal()
        return

    cidade = input("\nEm que cidade você reside? ")
    clearTerminal()
    endereco = input("\nQual é o seu endereço (rua)? ")
    clearTerminal()
    cep = input("\nDigite o seu CEP: ")

    # Adicionando os dados em um "dicionário"
    dicionarioPessoas = {
        "nome" : nome,
        "idade" : idade,
        "altura" : altura,
        "cidade" : cidade,
        "endereco" : endereco,
        "cep" : cep
    }

    # Adicionando todos os dados das pessoas dentro de uma lista
    listaPessoas.append(dicionarioPessoas)

    # Limpando terminal
    clearTerminal()

    # Mensagem de sucesso!
    print("\nPessoa cadastrada com suceso!")
    input("\nPressione a tecla ENTER para continuar...")
    clearTerminal()

def exibirCadastros(listaPessoas): # Exibindo informações...
    clearTerminal()
    print("\n====== EXIBIÇÃO DOS CADASTROS ======")
    if len(listaPessoas) == 0:
        clearTerminal()
        print("\nNão há nenhuma pessoa no sistema para exibir!")
    else:
        id = 0
        for pessoa in listaPessoas:
            print(f"\nID: {id}")
            print(f"NOME: {pessoa["nome"]}")
            print(f"IDADE: {pessoa["idade"]}")
            print(f"ALTURA: {pessoa["altura"]}")
            print(f"CIDADE: {pessoa["cidade"]}")
            print(f"ENDEREÇO: {pessoa["endereco"]}")
            print(f"CEP: {pessoa["cep"]}")
            id += 1

        print(f"\nTotal de pessoas no sistema: {id}")

    input("\nPressione a tecla ENTER para continuar...")
    clearTerminal()

def atualizar(listaPessoas): # Atualizando os dados de uma pessoa específica...
    pass

def excluir(listaPessoas): # Exclusão de alguma pessoa que já está no sistema...
    pass

def main():
    # Coração do projeto - Lista de "Pessoas"
    listaPessoas = []
    
    while True:
        clearTerminal()
        menu()

        # Tratar um possível erro do usuário - caso ele digite uma String (valueError).
        try:
            opcaoUsuario = int(input("\nDigite a opção desejada do menu: "))
        except ValueError:
            clearTerminal()
            print("\nOpção inválida para o menu - Só aceito números!")
            input("\nPressione a tecla ENTER para continuar...")
            continue
        else:
            # Estrutura Condicional chamando as funções com as operações do CRUD
            if (opcaoUsuario == 1):
                cadastrar(listaPessoas)
            elif (opcaoUsuario == 2):
                exibirCadastros(listaPessoas)
            elif (opcaoUsuario == 3):
                atualizar(listaPessoas)
            elif (opcaoUsuario == 4):
                excluir(listaPessoas)
            elif (opcaoUsuario == 5):
                clearTerminal()
                print("\n===== SAINDO DO PROGRAMA =====\n")
                break
            else:
                clearTerminal()
                print("\nOpção inválida para o menu!")
                input("\nPressione a tecla ENTER para continuar...")

if __name__ == "__main__":
    main()
