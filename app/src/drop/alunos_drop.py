import sqlite3
 
 
conexao = sqlite3.connect('gpsi.db')
cursor = conexao.cursor()

def drop_alunos():
    escolha = input("⚠️Desejas mesmo apagar a tabela alunos⚠️?(s ou n)")
    if(escolha == "s" | escolha == "S"):
        cursor.execute("DROP TABLE alunos;")
        print("\nTabela alunos apagada")

    elif (escolha == "n" | escolha == "N"):
        print("\nBoa escolha :)")

    else:
        print("\nEscolha inválida")
    
    conexao.commit()
    
    conexao.close()
 