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
    pass

def exibirCadastros(listaPessoas): # Exibindo informações...
    pass

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
                print("\nOpção inválida")

if __name__ == "__main__":
    main()
