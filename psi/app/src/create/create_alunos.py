import sqlite3

conexao = sqlite3.connect('C:\\Users\\ba2442\\Documents\\psi\\DB_Management\\psi\\app\\sqlite-database\\epbjc.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_aluno TEXT NOT NULL,
    idade_aluno INTEGER NOT NULL
)
''')

conexao.commit()
conexao.close()