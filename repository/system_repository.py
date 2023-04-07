import sqlite3

def system_table_init():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS system (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin INTEGER
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM system")
    count = cursor.fetchone()[0]
    #systemレコードが存在しない場合レコードを追加
    if count == 0:
        cursor.execute("INSERT INTO system (coin) VALUES (0)")
    conn.commit()
    conn.close()

def get_coin_num():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT coin FROM system WHERE id = 1")
    num = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return num

def update_coin(coin_value):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT coin FROM system WHERE id = 1")
    cursor.execute("UPDATE system SET coin = ? WHERE id = 1", (coin_value,))
    conn.commit()
    conn.close()