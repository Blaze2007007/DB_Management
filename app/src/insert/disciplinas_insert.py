import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def insert_disciplinas():

    disciplina1 = input("\nQual a disciplina que desejas inserir na tabela?")
    
    cur.execute(f'INSERT INTO disciplinas (disciplina) VALUES ({disciplina1})')
    
    conn.commit()