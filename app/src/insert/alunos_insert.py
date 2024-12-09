import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def insert_alunos():

    nome_aluno1 = input("\nQual o nome do aluno que desejas inserir na tabela?")
    idade_aluno1 = int(input("\nE a idade do mesmo?"))
    
    cur.execute(f'INSERT INTO alunos (nome_aluno, idade_aluno) VALUES ({nome_aluno1},{idade_aluno1})')
    
    conn.commit()