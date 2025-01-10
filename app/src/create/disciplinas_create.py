import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cur = conn.cursor()

def create_disciplinas():
    cur.execute(''' CREATE TABLE IF NOT EXISTS disciplinas(
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                disciplina TEXT NOT NULL,
                nome_aluno TEXT,
                nome_professor TEXT,

                FOREIGN KEY (nome_aluno) REFERENCES alunos(nome_aluno),
                FOREIGN KEY (nome_professor) REFERENCES professores(nome_professor)
                )''')

    conn.commit()
    conn.close()