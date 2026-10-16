def user_info():
    while True:
        user_nome = input("Digite o nome de usuário: ").strip()
        if not user_nome.isalpha():
            print("Nome de usuário deve conter somente **LETRAS**")
            print("Tente novamente.\n")

        elif len(user_nome) < 1:
            print("Esse campo deve ser preenchido!")
            print("Tente novamente!\n")

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
