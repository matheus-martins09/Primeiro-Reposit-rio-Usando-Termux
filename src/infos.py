from rich import print

def user_info():
    print("[bold green]Vamos criar um novo usuário![/]")
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
