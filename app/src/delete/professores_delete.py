import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def delete_professores():
    
    read_table_choice = int(input('''\nQue dados queres apagar da tabela professores?
                       \n1-Todos os dados
                       \n2-Apagar professores por nome
                       \n3-Apagar professores por id
                       \n4-Sair
                       '''))
    
    match (read_table_choice):
        case 1:

            cur.execute('DELETE * FROM professores')

            conn.commit()
        case 2:

            nome_professor1 = input('\nQual o nome do professor que desejas apagar?')

            cur.execute(f'DELETE nome_professor FROM professores WHERE nome_professor = {nome_professor1}')

            conn.commit()
        case 3:
            id_professor = input('\nQual o id do professor que pretendes apagar?')

            cur.execute(f'DELETE id FROM professores WHERE id = {id_professor}')

            conn.commit()
        case 4:
            conn.close()
        case _:
            print("Escolha inválida")