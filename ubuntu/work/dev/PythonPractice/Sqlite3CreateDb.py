import sqlite3

# 接続、存在しなければ新規作成
conn = sqlite3.connect('example.db')

# カーソル取得
cur = conn.cursor()

# personsテーブル作成
cur.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)')

# DBへコミット
conn.commit()
# DB接続解除
cur.close()
conn.close()