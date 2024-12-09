import sqlite3

conn = sqlite3.connect("gpsi.db")
cur = conn.cursor()

def create_disciplinas():
    cur.execute(''' CREATE TABLE IF NOT EXISTS disciplinas(
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                disciplina TEXT NOT NULL
                )''')

    conn.commit()
    conn.close()