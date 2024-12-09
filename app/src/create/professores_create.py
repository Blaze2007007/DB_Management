import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def create_professores():
    cur.execute(''' CREATE TABLE IF NOT EXISTS professores(
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_professor TEXT NOT NULL
                )''')

    conn.commit()
    conn.close()