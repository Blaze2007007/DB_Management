import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cur = conn.cursor()

def update_alunos():

    escolha_id = int(input("Qual o id do aluno que desejas atualizar?"))

    escolha_nome = input("Qual o nome com o qual queres trocar?")
    escolha_idade = int(input("Qual a idade com o qual queres trocar?"))

    cur.execute(f'UPDATE alunos SET nome_aluno = "{escolha_nome}" WHERE id = {escolha_id}')
    cur.execute(f'UPDATE alunos SET idade_aluno = {escolha_idade} WHERE id = {escolha_id}')
    
    conn.commit()

    conn.close()