# Limite de caracteres definido para 88 (Padrão comunitário)
# PEP 8 recomenda 79 como limite. Mas também nos permite ir até um limite de 100

# PADRÕES DO CÓDIGO
# variáveis utilizam o modelo "snake_case" recomendado pela PEP 8
# TODAS as variáveis começam com alguma palavra em inglês e terminal com português
# Exemplo: user_nome

# FUNÇÕES seguem o mesmo modelo de "snake_case". Mas são deckaradas somente em inglês

# Estou fazendo o programa dessa forma (usando "main()") para não fugir do padrão
# C/C++ e Java


from rich import print


def user_info():
    while True:
        user_nome = input("Digite o nome de usuário: ").strip()
        if len(user_nome) < 1:
            print("[/yellow]Esse campo deve ser [bold]PREENCHIDO[/bold][/yellow]")
            print("Tente novamente.\n")

        elif not user_nome.isalpha():
            print("Nome de usuário deve conter somente [bold]LETRAS[/bold]")
            print("Tente novamente.\n")

        else:
            print("Nome salvo com sucesso!")
            break

    return user_nome


def main():
    print("Olá, mundo!")
    user_nome = user_info()
    print(f"Usuário logado: {user_nome}")


if __name__ == "__main__":
    main()
