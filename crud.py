# CRUD em Python para realizar operações (create - read - update - delete)

# Cadastro de uma pessoa com dados básicos como (nome, idade, altura, cidade, endereço e cep)

# ====== Importações ======
import os

# Função para limpar o terminal assim que ela for chamada
def clearTerminal():
    os.system("cls")

# Função para exibir o menu para o usuário
def menu():
    print("\n1 - Cadastrar uma pessoa no sistema")
    print("2 - Exibir cadastros")
    print("3 - Atualizar dados de uma pessoa")
    print("4 - Excluir uma pessoa do sistema")
    print("5 - Sair do sistema")



def main():
    while True:
        clearTerminal()
        menu()
        # Tratar um possível erro do usuário
        try:
            opcaoUsuario = int(input("\nDigite a opção desejada do menu: "))
        except ValueError:
            clearTerminal()
            print("\nOpção inválida para o menu - Só aceito números!")
            input("\nPressione a tecla ENTER para continuar...")
            continue


if __name__ == "__main__":
    main()
