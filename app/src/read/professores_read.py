import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")

cur = conn.cursor()

def read_professores():
    read_table_choice = int(input('''\nO que queres ler nesta tabela?
                       \n1-Todos os dados
                       \n2-Pesquisar professores por nome
                       \n3-Pesquisar professores por id
                       \n4-Sair
                       '''))
    
    match (read_table_choice):
        case 1:
            cur.execute('SELECT * FROM professores')

            resultados = cur.fetchall()

            for aluno in resultados:
                print(aluno)
        case 2:
            nome_professor1 = input('\nQual o professor que procuras(nome)?')

            cur.execute(f'SELECT nome_professor FROM professores WHERE nome_professor = {nome_professor1}')

            resultados = cur.fetchall()

            for professor in resultados:
                print(professor)
        case 3:
            id_professor1 = input('\nQual o professor que procuras(id)?')

            cur.execute(f'SELECT id FROM professores WHERE id = {id_professor1}')

            resultados = cur.fetchall()

            for professor in resultados:
                print(professor)
        case 4:
            conn.close()
    