import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cur = conn.cursor()

def innerjoin_alunos():
    cur.execute("SELECT * FROM alunos INNER JOIN disciplinas ON alunos.id_disciplina = disciplinas.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

conn.commit()