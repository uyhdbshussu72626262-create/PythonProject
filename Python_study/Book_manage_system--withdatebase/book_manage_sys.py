# 图书馆的管理图表系统--用SQlite数据库实现
from permission import permission_guard, PermissionManager
from repository import *

class Book_manager:

    def __init__(self):
        self.is_login = False

#图书管理员登录
    def login(self):
        manager_id = input("管理员编号:")
        password = input("密码:")
        if verify_manager(manager_id, password):
            self.is_login = True
            PermissionManager.set_role("admin")
            print("登录成功")
        else:
            print("登录失败")

    # 图书管理员注册
    def new_book_manager_register(self):
        id = input("请输入id:")
        name = input("员工名称:")
        manager_id = input("管理员编号:")
        password = input("密码:")
        success = manager_register(id, name, manager_id, password)
        print("注册成功" if success else "注册失败")

#添加图书
    def manager_add_book(self):
        if not self.is_login:
            print("请先登录")
            return
        book_name = input("书名:")
        author = input("作者:")
        publish_date = input("出版时间:")
        book_type = input("书籍类型:")
        success = add_book(book_name, author, publish_date, book_type)
        print("添加成功" if success else "添加失败")

#删除图书
    def manager_delete_book(self):
        if not self.is_login:
            print("请先登录")
            return
        book_code = input("图书编号:")
        success = delete_book(book_code)
        print("删除成功" if success else "删除失败")

#删除用户
    def manager_cancel_user_borrow_right(self):
        if not self.is_login:
            print("请先登录")
            return
        user_name = input("用户名:")
        success = cancel_user(user_name)
        print("删除成功" if success else "删除失败")


class User:

#普通用户注册
    def new_user_register(self):
        user_id = input("用户id:")
        username = input("用户名:")
        password = input("密码:")
        success = user_register(user_id, username, password)
        print("注册成功" if success else "注册失败")

#普通用户登录
    def login(self):
        username = input("用户名:")
        password = input("密码:")
        if verify_user(username, password):
            PermissionManager.set_role("user")
            print("登录成功")
        else:
            print("登录失败")


class Show:

#查任意一本书
    def show_any_book(self, book_name):
        book = show_any_book(book_name)
        if not book:
            print("未找到该书")
            return
        print(f"书名:{book['book_name']}")
        print(f"作者:{book['author']}")
        print(f"出版时间:{book['publish_date']}")
        print(f"类型:{book['book_type']}")

#查书集合
    def show_book_set(self):
        books = show_book_set()
        if not books:
            print("无图书")
            return
        for book in books:
            print("-" * 30)
            print(f"书名:{book['book_name']}")
            print(f"作者:{book['author']}")
            print(f"出版时间:{book['publish_date']}")
            print(f"类型:{book['book_type']}")

#查用户
    def show_user_set(self):
        users = show_user_set()
        if not users:
            print("无用户")
            return
        for user in users:
            print("-" * 30)
            print(f"用户名:{user['username']}")
            print(f"用户ID:{user['id']}")

#查管理员结合
    def show_manager_set(self):
        managers = show_manager_set()
        if not managers:
            print("无管理员")
            return
        for manager in managers:
            print("-" * 30)
            print(f"管理员名称:{manager['name']}")
            print(f"管理员编号:{manager['manager_id']}")


def print_menu():
    print("\n图书管理系统")
    print("1. 用户注册")
    print("2. 管理员注册")
    print("3. 用户登录")
    print("4. 管理员登录")
    print("5. 添加图书")
    print("6. 删除图书")
    print("7. 删除用户")
    print("8. 查询某本书")
    print("9. 查看所有图书")
    print("10. 查看用户列表")
    print("11. 查看管理员列表")
    print("0. 退出")

@permission_guard
def main():
    manager = Book_manager()
    user = User()
    show = Show()

    while True:
        print_menu()
        try:
            number = int(input("选择功能:"))
        except ValueError:
            print("输入错误")
            continue

        if number == 1:
            user.new_user_register()
        elif number == 2:
            manager.new_book_manager_register()
        elif number == 3:
            user.login()
        elif number == 4:
            manager.login()
        elif number == 5:
            manager.manager_add_book()
        elif number == 6:
            manager.manager_delete_book()
        elif number == 7:
            manager.manager_cancel_user_borrow_right()
        elif number == 8:
            book_name = input("书名:")
            show.show_any_book(book_name)
        elif number == 9:
            show.show_book_set()
        elif number == 10:
            show.show_user_set()
        elif number == 11:
            show.show_manager_set()
        elif number == 0:
            print("系统退出")
            break
        else:
            print("无效输入")


if __name__ == "__main__":
    main()



