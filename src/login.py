from infos import user_info
from rich import print
import sqlite3

def verification_user(nome: str):
    if nome is None:
        print("Usuário não encontrado!")

        user_nome, password, browser_principal = user_info()

        return user_nome, password, browser_principal

    else:
        conexao = sqlite3.connect("system-infos.db")
        cursor = conexao.cursor()
