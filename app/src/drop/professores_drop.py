import sqlite3
 
 
conexao = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")
cursor = conexao.cursor()

def drop_professores():
    escolha = input("⚠️Desejas mesmo apagar a tabela professores⚠️?(s ou n)")
    if(escolha == "s" | escolha == "S"):
        cursor.execute("DROP TABLE professores;")
        print("\nTabela professores apagada")

    elif (escolha == "n" | escolha == "N"):
        print("\nBoa escolha :)")

    else:
        print("\nEscolha inválida")
    
    conexao.commit()
    
    conexao.close()