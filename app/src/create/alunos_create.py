import sqlite3 #Importar biblioteca sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db") #Criar a variável conn para fazer a conexão à base de dados gpsi.db
cur = conn.cursor() #Criar cursor para executar QUERIES

def create_alunos(): #Criar a função(create_alunos) para ser chamada no programa principal

    #Criar tabela alunos para armazenamento dos dados do aluno(id chave primária autoincrementada, nome do aluno obrigatório e idade do aluno obrigatória)
    cur.execute(''' CREATE TABLE IF NOT EXISTS alunos(
                id          INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome_aluno  TEXT NOT NULL,
                idade_aluno INTEGER NOT NULL,
                )''')

    conn.commit() #Gravar alterações na base de dados
    conn.close() #Fechar a ligação com a base de dados

