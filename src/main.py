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
import hashlib


def create_database():
    with sqlite3.connect("system-infos.db") as conexao:
        cursor = conexao.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS informacoes-sistema (
                user_nome TEXT NOT NULL,
                password TEXT NOT NULL,
                browser TEXT NOT NULL
            )  
            """)
        
        conexao.commit()


def hash_generation(user_nome: str, passaword: str):
    byte_nome = user_nome.encode("utf-8")
    hash_nome = hashlib.sha256(byte_nome)

    byte_password = passaword.encode("utf-8")
    hash_password = hashlib.sha256(byte_password)

    return hash_nome.hexdigest(), hash_password.hexdigest()


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

    while True:
        print("Vamos criar uma senha para o usuário!")
        password = input("Insira a senha de usuário: ").strip()

        if len(password) < 1:
            print("[yellow]Esse campo deve ser [bold]PREENCHIDO[/bold][/yellow]")

        else:
            print("Senha salva com sucesso!")
            break

    browser_lista = ["firefox", "google-chrome", "microsoft-edge"]

    while True:
        print("=" * 30)
        print(f"{"Navegador Principal":^30}")
        print("=" * 30)
        print("Firefox [1]\nGoogle Chrome [2]\nMicrosoft Edge [3]")
        print("-" *30)

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

    return user_nome, password, browser_principal


def main():
    user_nome, password, browser_principal = user_info()
    hash_nome, hash_pass = hash_generation(user_nome, password)


if __name__ == "__main__":
    main()

