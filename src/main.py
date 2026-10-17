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
from login import verification_user
from hash import hash_generation


def create_database(cursor):
    conexao = sqlite3.connect("database/system-infos.db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS informacoes_sistema (
            user_nome TEXT NOT NULL,
            password TEXT NOT NULL,
            browser TEXT NOT NULL
        )  
        """)
    conexao.commit()


def update_database(user_nome: str, hash_pass: str, browser: str):
    conexao = sqlite3.connect("database/system-infos.db")
    cursor = conexao.cursor()

    cursor.execute(
    "INSERT INTO informacoes_sistema(user_nome, password, browser) VALUES(?, ?, ?)",
    (user_nome, hash_pass, browser),
    )

    conexao.commit()


def main():
    conexao = sqlite3.connect("database/system-infos.db")
    cursor = conexao.cursor()

    create_database(cursor)

    cursor.execute("SELECT user_nome FROM informacoes_sistema LIMIT 1")
    user_nome = cursor.fetchone()

    user_nome, password, browser_principal = verification_user(user_nome)
    hash_pass = hash_generation(password)

    update_database(user_nome, hash_pass, browser_principal)

    conexao.close()

if __name__ == "__main__":
    main()
