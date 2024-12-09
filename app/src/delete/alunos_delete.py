import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def delete_alunos():

    delete_table_choice = int(input('''\nQue dados desejas apagar da tabela alunos?
                       \n1-Todos os dados
                       \n2-Apagar alunos por nome
                       \n3-Apagar alunos por nome e idade
                       \n4-Sair
                       '''))
    
    match (delete_table_choice):
        case 1:

            cur.execute('DELETE * FROM alunos')

            conn.commit()

        case 2:

            nome_aluno1 = input('\nQual o nome do aluno que desejas apagar?')

            cur.execute(f'Delete nome_aluno FROM alunos WHERE nome_aluno = {nome_aluno1}')

            conn.commit()
        case 3:
            nome_aluno2 = input('\nQual o nome do aluno que desejas apagar?')
            idade_aluno = input('\nE a idade do mesmo?')

            cur.execute(f'DELETE nome_aluno FROM alunos WHERE nome_aluno = {nome_aluno2} AND idade_aluno = {idade_aluno} ')

            conn.commit()
        case 4:
            conn.close()
        case _:
            print("Escolha inválida")