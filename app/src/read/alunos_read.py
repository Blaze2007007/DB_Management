import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")

cur = conn.cursor()

def read_alunos():
    read_table_choice = int(input('''\nO que queres ler nesta tabela?
                       \n1-Todos os dados
                       \n2-Pesquisar alunos por nome
                       \n3-Pesquisar alunos por nome e idade
                       \n4-Perquisar alunos por id
                       \n5-Sair
                       '''))
    
    match (read_table_choice):
        case 1:

            cur.execute('SELECT * FROM alunos')

            resultados = cur.fetchall()

            for aluno in resultados:
                print(aluno)
        case 2:

            nome_aluno1 = input('\nQual o nome do aluno que procuras?')

            cur.execute(f'SELECT nome_aluno FROM alunos WHERE nome_aluno = {nome_aluno1}')

            resultados = cur.fetchall()

            for aluno in resultados:
                print(aluno)
        case 3:
            nome_aluno2 = input('\nQual o nome do aluno que procuras?')
            idade_aluno = input('\nQual a idade aluno que procuras?')

            cur.execute(f'SELECT nome_aluno FROM alunos WHERE nome_aluno = {nome_aluno2} AND idade_aluno = {idade_aluno} ')

            resultados = cur.fetchall()

            for aluno in resultados:
                print(aluno)

        case 4:

            id_aluno1 = input('\nQual o id do aluno que procura?')

            cur.execute(f'SELECT id FROM alunos WHERE id = {id_aluno1}')

            resultados = cur.fetchall()

            for aluno in resultados:
                print(aluno)

        case 5:
            ""
    