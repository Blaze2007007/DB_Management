import sqlite3
 
con = sqlite3.connect('C:\\Users\\ba2442\\Documents\\psi\\DB_Management\\psi\\app\\sqlite-database\\epbjc.db')
cur = conexao.cursor()
 
cursor.execute('''
CREATE TABLE IF NOT EXISTS disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    disciplina TEXT NOT NULL
)
''')
 
conexao.commit()
 
conexao.close()