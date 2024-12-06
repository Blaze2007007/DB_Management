import sqlite3
 
con = sqlite3.connect('C:\\Users\\ba2442\\Documents\\psi\\DB_Management\\psi\\app\\sqlite-database\\epbjc.db')
cur = conexao.cursor()
 
cursor.execute('''
CREATE TABLE IF NOT EXISTS professores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_professor TEXT NOT NULL,
)
''')
 
conexao.commit()
 
conexao.close()