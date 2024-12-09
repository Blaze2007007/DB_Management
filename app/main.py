import sqlite3
import os
import sys

#------------------------------------------------------------#
from src.create.alunos_create import create_alunos           #
from src.create.disciplinas_create import create_disciplinas #
from src.create.professores_create import create_professores #
#------------------------------------------------------------#
from src.insert.alunos_insert import insert_alunos           #
from src.insert.disciplinas_insert import insert_disciplinas #
from src.insert.professores_insert import insert_professores #
#------------------------------------------------------------#
from src.read.alunos_read import read_alunos                 #
from src.read.disciplinas_read import read_disciplinas       #
from src.read.professores_read import read_professores       #
#------------------------------------------------------------#
from src.delete.alunos_delete import delete_alunos           #
from src.delete.disciplinas_delete import delete_disciplinas #
from src.delete.professores_delete import delete_professores #
#------------------------------------------------------------#
from src.drop.alunos_drop import drop_alunos                 #
from src.drop.disciplinas_drop import drop_disciplinas       #
from src.drop.professores_drop import drop_professores       #
#------------------------------------------------------------#
from src.insert.alunos_insert import insert_alunos           #
from src.insert.disciplinas_insert import insert_disciplinas #
from src.insert.professores_insert import insert_professores #
#------------------------------------------------------------#

conn = sqlite3.connect("C:\\Users\\Jorge Silva\\OneDrive\\Documentos\\epbjc\\sqlite-database\\gpsi.db")

escolha_da_tabela = int(input('''\nQual é a tabela que queres usar?
                       \n1-Alunos
                       \n2-Disciplinas
                       \n3-Professores
                       '''))

nome_da_tabela = ""
match (escolha_da_tabela):
        case 1:
            opcaocrd = int(input('''\nO que queres fazer nesta tabela?
                       \n1-Criar tabela alunos
                       \n2-Inserir dados na tabela
                       \n3-Ler tabela
                       \n4-Apagar dados da tabela
                       \n5-Apagar tabela
                       \n6-Voltar 
                       '''))
            
            match(opcaocrd):
                    case 1:
                        create_alunos()
                    case 2:
                        insert_alunos()
                    case 3:
                        read_alunos()
                    case 4:
                        delete_alunos()
                    case 5:
                        drop_alunos()
                    case 6:
                        conn.close()
                    case _:
                        print("Escolha inválida")
                 
        case 2:
            opcaocrd = int(input('''\nO que queres fazer nesta tabela?
                       \n1-Criar tabela disciplinas
                       \n2-Inserir dados na tabela
                       \n3-Ler tabela
                       \n4-Apagar dados da tabela
                       \n5-Apagar tabela
                       \n6-Voltar  
                       '''))
            
            match(opcaocrd):
                    case 1:
                        create_disciplinas()
                    case 2:
                        insert_disciplinas()
                    case 3:
                        read_disciplinas()
                    case 4:
                        delete_disciplinas()
                    case 5:
                        drop_disciplinas()
                    case 6:
                      conn.close()
                    case _:
                        print("Escolha inválida")
        case 3:
            opcaocrd = int(input('''\nO que queres fazer nesta tabela?
                       \n1-Criar tabela professores
                       \n2-Inserir dados na tabela
                       \n3-Ler tabela
                       \n4-Apagar dados da tabela
                       \n5-Apagar tabela
                       \n6-Voltar 
                       '''))
            
            match(opcaocrd):
                    case 1:
                        create_professores()
                    case 2:
                        insert_professores()
                    case 3:
                        read_professores()
                    case 4:
                        delete_professores()
                    case 5:
                        drop_professores()
                    case 6:
                      conn.close()
                    case _:
                        print("Escolha inválida")
        case _:
          print("Escolha inválida")

conn.commit()
conn.close()