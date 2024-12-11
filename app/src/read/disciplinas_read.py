import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")

cur = conn.cursor()

def read_disciplinas():
    read_table_choice = int(input('''\nO que queres ler nesta tabela?
                       \n1-Todos os dados
                       \n2-Pesquisar disciplinas
                       \n3-Sair
                       '''))
    
    match (read_table_choice):
        case 1:
            cur.execute('SELECT * FROM disciplinas')

            resultados = cur.fetchall()

            for aluno in resultados:
                print(aluno)
        case 2:
            disciplina = input('\nQual a disciplina que procuras?')

            cur.execute(f'SELECT disciplina FROM disciplinas WHERE disciplina = {disciplina}')

            resultados = cur.fetchall()

            for disciplinas in resultados:
                print(disciplinas)
        case 3:
            ""
    