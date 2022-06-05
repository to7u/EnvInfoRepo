import sqlite3

db_name = 'example.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

cur.execute('SELECT * FROM persons')

# 中身を全て取得するfetchall()を使って、printする。
print(cur.fetchall())

cur.close()
conn.close()