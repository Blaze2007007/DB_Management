import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def update_alunos():

    escolha_id = int(input("Qual a disciplina que desejas atualizar?"))

    escolha_nome = input("Qual a disciplina com a qual queres trocar?")
    escolha_idade = int(input("Qual a idade com o qual queres trocar?"))

    cur.execute(f'UPDATE alunos SET nome_aluno = {escolha_nome} AND WHERE id = {escolha_id}')
    cur.execute(f'UPDATE alunos SET idade_aluno = {escolha_idade} AND WHERE id = {escolha_id}')