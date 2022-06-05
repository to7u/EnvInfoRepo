import sqlite3

# DBをメモリ上に作成する
conn = sqlite3.connect(":memory")
cur = conn.cursor()

# DB操作処理

# クローズするとDBも削除される
conn.close()