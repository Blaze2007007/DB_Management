import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cur = conn.cursor()

def update_professores():

    escolha_id = int(input("Qual o id do professor que desejas atualizar?"))

    escolha_professor = input("Qual o nome do professor com o qual queres trocar?")

    cur.execute(f'UPDATE professores SET nome_professor = "{escolha_professor}" WHERE id = {escolha_id}')

    conn.commit()

    conn.close()