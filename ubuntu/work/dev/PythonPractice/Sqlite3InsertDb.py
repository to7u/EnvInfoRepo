import sqlite3

db_name = 'example.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

cur.execute('INSERT INTO persons(name) values("Taro")')
cur.execute('INSERT INTO persons(name) values("Hanako")')
cur.execute('INSERT INTO persons(name) values("Hiroki")')

conn.commit()

cur.close()
conn.close()