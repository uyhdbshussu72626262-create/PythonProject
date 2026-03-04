#数据库操作文件
from date_models import get_conn
import sqlite3
import hashlib
import uuid

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


#管理员注册账户
def manager_register(id,book_manager_name,book_manager_ID,manager_password):

    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            hashed_pwd = _hash_password(manager_password)
            cursor.execute(
                "INSERT INTO managers(id,name,manager_id,password) VALUES (?,?,?,?)",
                (id,book_manager_name,book_manager_ID,hashed_pwd)
            )
            return True
    except sqlite3.IntegrityError:
        return False
    except sqlite3.Error:
        return False

#管理员上传书籍
#1.为书籍生成唯一编号
def generate_unique_book_id():
    return str(uuid.uuid4())[:10]
            # 生成10位随机数

def add_book(book_name, author, publish_date, book_type):
     try:
         with get_conn() as conn:
          cursor = conn.cursor()
          book_code = generate_unique_book_id()
          cursor.execute(
            """
            INSERT INTO books
            (book_name,book_code,author,publish_date,book_type)
            VALUES (?,?,?,?,?)""",
            (book_name,book_code,author,publish_date,book_type)     
          )
         return True
     except sqlite3.Error:
         return False

def delete_book(book_code):
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                    "DELETE FROM books where book_code =?",
                    (book_code,)
            )
            return cursor.rowcount>0
    except sqlite3.Error:
        return False

def cancel_user(user_name):
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                    "DELETE FROM user where username=?",
                    (user_name,)
            )
            return cursor.rowcount>0
    except sqlite3.Error:
            return False

#用户的注册
def user_register(id, username, password):
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            hashed_pwd = _hash_password(password)
            cursor.execute(
                "INSERT INTO user(id,username,password) VALUES(?,?,?)",
                (id, username, hashed_pwd)
            )
            return True
    except sqlite3.IntegrityError:
        return False
    except sqlite3.Error:
        return False




#用户的登录验证

def verify_user(username, password):
    try:
        with get_conn() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM user WHERE username=?",
                (username,)
            )
            user = cursor.fetchone()
            if user and user["password"] == _hash_password(password):
                return True
            return False
    except sqlite3.Error:
        return False

def verify_manager(manager_id, password):
    try:
        with get_conn() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM managers WHERE manager_id=?",
                (manager_id,)
            )
            manager = cursor.fetchone()
            if manager and manager["password"] == _hash_password(password):
                return True
            return False
    except sqlite3.Error:
        return False

#数据查询--通过通用的数据库查询查看
#1.查询任意一本书
def show_any_book(book_name):
    try:
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT
                    id,
                    book_name,
                    book_code,
                    author,
                    publish_date,
                    book_type
                FROM books
                WHERE book_name=?
                """,
                (book_name,)
            )
            row = cursor.fetchone()
            if not row:
                return None

            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, row))

    except sqlite3.Error:
        return None


#2.查询所有书籍列表
def show_book_set():
    try:
        with get_conn() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
            "SELECT * FROM books"
            )
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in rows]

    except sqlite3.Error:
        return []

#3.查询用户列表
def show_user_set():
    try:
        with get_conn() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
    except sqlite3.Error:
        return []

#4.查询图书管理员列表
def show_manager_set():
    try:
        with get_conn() as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM managers")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
    except sqlite3.Error:
        return []
