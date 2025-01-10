import sqlite3 #Importar biblioteca sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db") #Criar a variável conn para fazer a conexão à base de dados gpsi.db
cur = conn.cursor() #Criar cursor para executar QUERIES

def create_professores(): #Criar a função(create_professores) para ser chamada no programa principal

    #Criar tabela professores para armazenamento dos dados do professor(id chave primária autoincrementada, nome do professor obrigatório)
    cur.execute(''' CREATE TABLE IF NOT EXISTS professores(
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_professor TEXT NOT NULL,
                )''')

    conn.commit() #Gravar alterações na base de dados
    conn.close() #Fechar a ligação com a base de dados