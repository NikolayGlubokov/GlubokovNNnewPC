import csv
import sqlite3 as sq


c = []
with open('forhomework44.csv', 'r') as r_file:

    file_reader=csv.reader(r_file, delimiter=';')
    for row in file_reader:
        c.append(row)



with sq.connect('homeworkdatabase44.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS hw44gnn(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    goods_name TEXT NOT NULL,
    not_sell_price REAL,
    sell_price REAL,
    ball REAL,
    sell_value TEXT
    )''')
    cur.executemany('INSERT INTO hw44gnn VALUES(NULL,?,?,?,?,?)',c)

