import sqlite3 #Importar biblioteca sqlite3

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db") #Criar a variável conn para fazer a conexão à base de dados gpsi.db
cur = conn.cursor() #Criar cursor para executar QUERIES

def create_disciplinas(): #Criar a função(create_disciplinas) para ser chamada no programa principal

    #Criar tabela disciplinas para armazenamento dos dados das disciplinas(id chave primária autoincrementada, disciplinas obrigatória, nome do aluno que tem a disciplina(chave estrangeira da tabela alunos),nome do professor que ensina a disciplina(chave estrangeira da tabela professores))
    cur.execute(''' CREATE TABLE IF NOT EXISTS disciplinas(
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                disciplina TEXT NOT NULL,
                nome_aluno TEXT,
                nome_professor TEXT,

                FOREIGN KEY (nome_aluno) REFERENCES alunos(nome_aluno),
                FOREIGN KEY (nome_professor) REFERENCES professores(nome_professor)
                )''')

    conn.commit() #Gravar alterações na base de dados
    conn.close() #Fechar a ligação com a base de dados