import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cur = conn.cursor()

def insert_professores():

    nome_professor1 = input("\nQual o nome do professor que desejas inserir na tabela?")
    
    cur.execute(f'INSERT INTO professores (nome_professor) VALUES ("{nome_professor1}")')
    
    conn.commit()