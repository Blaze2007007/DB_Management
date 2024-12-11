import sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cur = conn.cursor()

def delete_disciplinas():
    
    delete_table_choice = int(input('''\nQue dados desejas apagar da tabela disciplinas?
                       \n1-Todas as disciplinas
                       \n2-Apagar disciplina
                       \n3-Sair
                       '''))
    
    match (delete_table_choice):
        case 1:
            escolha = input("⚠️Desejas mesmo apagar todas as disciplinas⚠️?(s ou n)")

            if(escolha == "s" | escolha == "S"):

                cur.execute('DELETE * FROM disciplinas')
                print("\nDisciplinas apagadas")

            elif (escolha == "n" | escolha == "N"):

                print("\nBoa escolha :)")

            else:
                print("\nEscolha inválida")
                

        case 2:

            disciplina1 = input('\nQual a disciplina que desejas apagar?')

            escolha = input("⚠️Desejas mesmo apagar esta disciplina⚠️?(s ou n)")

            if(escolha == "s" | escolha == "S"):

                cur.execute(f'DELETE disciplina FROM disciplinas WHERE disciplina = {disciplina1}')
                print("\nDisciplina apagada")

            elif (escolha == "n" | escolha == "N"):

                print("\nBoa escolha :)")

            else:
                print("\nEscolha inválida")

        case 3:
            ""
        case _:
            print("Escolha inválida")

conn.commit()