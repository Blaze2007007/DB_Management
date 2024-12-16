import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cur = conn.cursor()

def update_disciplinas():

    escolha_id = int(input("Qual o id da disciplina que desejas atualizar?"))

    escolha_disciplina = input("Qual a disciplina com a qual queres trocar?")

    cur.execute(f'UPDATE disciplinas SET disciplina = "{escolha_disciplina}" WHERE id = {escolha_id}')

    conn.commit()

    conn.close()