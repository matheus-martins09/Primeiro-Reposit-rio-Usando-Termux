# Limite de caracteres definido para 88 (Padrão comunitário)
# PEP 8 recomenda 79 como limite. Mas também nos permite ir até um limite de 100

# PADRÕES DO CÓDIGO
# variáveis utilizam o modelo "snake_case" recomendado pela PEP 8
# TODAS as variáveis começam com alguma palavra em inglês e terminal com português
# Exemplo: user_nome

# FUNÇÕES seguem o mesmo modelo de "snake_case". Mas são declaradas somente em inglês

# Estou fazendo o programa dessa forma (usando "main()") para não fugir do padrão
# C/C++ e Java


#Bibliotecas
import sqlite3
from rich import print


def user_info():
    while True:
        user_nome = input("Digite o nome de usuário: ").strip()
        if len(user_nome) < 1:
            print("[yellow]Esse campo deve ser [bold]PREENCHIDO[/bold][/yellow]")
            print("Tente novamente.\n")

        elif not user_nome.isalpha():
            print("Nome de usuário deve conter somente [bold]LETRAS[/bold]")
            print("Tente novamente.\n")

        else:
            print("Nome salvo com sucesso!")
            break

    browser_lista = ["firefox", "google-chrome", "microsoft-edge"]

    while True:
        print("=" * 30)
        print(f"{"Navegador Principal":^30}")
        print("=" * 30)
        print("Firefox [1]\nGoogle Chrome [2]\nMicrosoft Edge [3]")

        browser_principal = input("Digite a opção correspondente: ").strip()

        if len(browser_principal) < 1:
            print("[yellow]Esse deve ser PREENCHIDO[/yellow]")
            print("Tente novamente.\n")

        elif not browser_principal.isnumeric():
            print("[red]O que você digiou não é um [bold]NÚMERO[/bold][/red]")
            print("Tente novamemte.\n")

        elif browser_principal[0] in "1234":
            browser_principal = browser_principal[0]

            match browser_principal:
                case "1":
                    browser_principal = browser_lista[0]
                    break

                case "2":
                    browser_principal = browser_lista[1]
                    break

                case "3":
                    browser_principal = browser_lista[2]
                    break

    return user_nome, browser_principal


def main():
    print("Olá, mundo!")
    user_nome, browser_principal = user_info()
    print(f"Usuário logado: {user_nome}")
    print(f"Navegador principal: {browser_principal}")


if __name__ == "__main__":
    main()

