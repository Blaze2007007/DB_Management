import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def create_alunos():
    cur.execute(''' CREATE TABLE IF NOT EXISTS alunos(
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_aluno  TEXT NOT NULL,
                idade_aluno INTEGER NOT NULL
                )''')

    conn.commit()
    conn.close()

