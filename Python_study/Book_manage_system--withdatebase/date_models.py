import sqlite3

def get_conn():
    return sqlite3.connect("library.db")

def init_db():
    conn = get_conn()
    cursor = conn.cursor()


#用户的数据存储数据库
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id integer primary key autoincrement,
        username text unique,
        password text
    )
""")
    
#管理员的数据存储数据库
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS managers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        manager_id TEXT,
        password TEXT
    )
    """)

#书籍的存储数据库
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_name TEXT UNIQUE,
        book_code TEXT,
        author TEXT,
        publish_date TEXT,
        book_type TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__=="__main__":
    init_db()
    print("数据库初始化完成")