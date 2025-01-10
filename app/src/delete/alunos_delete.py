import sqlite3 #Importar biblioteca sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db") #Criar a variável conn para fazer a conexão à base de dados gpsi.db
cur = conn.cursor() #Criar cursor para executar QUERIES

def delete_alunos(): #função o para apagar dados da tabela alunos.

    #Pede ao utilizador que escolha se deseja apagar todos os dados da tabela, apagar dados por nome, apagar dados por id, apagar dados por nome e idade ou sair.
    delete_table_choice = int(input('''\nQue dados desejas apagar da tabela alunos?
                       \n1-Todos os dados 
                       \n2-Apagar alunos por nome                                  
                       \n3-Apagar alunos por id
                       \n4-Apagar alunos por nome e idade
                       \n5-Sair
                       '''))
    
    match (delete_table_choice):
        case 1: #Se o utilizador escolher apagar todos os dados, apaga todos os dados da tabela.
            cur.execute('DELETE * FROM alunos')

        case 2: #Se o utilizador escolher apagar dados por nome, pede o nome do aluno que deseja apagar e apaga todas as entradas com esse nome.
            nome_aluno1 = input('\nQual o nome do aluno que desejas apagar?')

            cur.execute(f'Delete nome_aluno FROM alunos WHERE nome_aluno = {nome_aluno1}')

        case 3: #Se o utilizador escolher apagar dados por id, pede o id do aluno que deseja apagar e apaga todas as entradas com esse id.

            id_aluno1 = input('\nQual o id do aluno que desejas apagar?')

            cur.execute(f'DELETE nome_aluno FROM alunos WHERE nome_aluno = {nome_aluno2} AND idade_aluno = {idade_aluno} ')

        case 4: #Se o utilizador escolher apagar dados por nome e idade, pede o nome e a idade do aluno que deseja apagar e apaga todas as entradas com esse nome e idade.

            nome_aluno2 = input('\nQual o nome do aluno que desejas apagar?')
            idade_aluno = input('\nE a idade do mesmo?')

            cur.execute(f'DELETE nome_aluno FROM alunos WHERE nome_aluno = {nome_aluno2} AND idade_aluno = {idade_aluno} ')

        case 5: #Se o utilizador escolher sair, sai da função sem fazer nada.
            ""
        case _: #Caso o utilizador escolha uma opção o inválida, imprime uma mensagem de erro e sai da função.
            print("Escolha inválida")

conn.commit() #Gravar alterações na base de dados