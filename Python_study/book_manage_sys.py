#面向过程的公共图书管理系统


# 面向过程的公共图书管理系统

user_data = {}
book_set = {}


def new_user_register():
    user_name = input("创建用户名为:")
    password = input("(请确认环境是否安全)创建密码为:")
    user_data[user_name] = password
    print(f"用户 {user_name} 注册成功！")


def old_user_login():
    return "欢迎再次光临本馆，请输入指令进入其他环节"


def add_book():
    book_name = input("书本名称为:")
    if book_name in book_set:
        print("本书已被存入")
    else:
        author = input("作者为:")
        publish_date = input("出版时间为:")

        book_set[book_name] = {
            "作者": author,
            "出版时间": publish_date
        }
        print(f"加入《{book_name}》成功")


def show_any_book(book_name):
    if book_name in book_set:
        info = book_set[book_name]
        print(f"书名：{book_name}")
        print(f"作者：{info['作者']}")
        print(f"出版时间：{info['出版时间']}")
    else:
        print("抱歉，本馆还没有这本书")


def show_book_set():
    print(f"{book_set}")


print("欢迎进入本图书馆，\n")
print("本图书馆书籍丰富，环境良好，\n")
print("是个学习放松的好地方.\n")
# 新用户注册登录介绍用于
print("新用户请根据提示指令注册为本图书馆的用户")
print("|---1.注册新用户---|")
print("|---2.老用户登录---|")
print("|---3.用户添加图书---|")
print("|---4.查看某本图书---|")
print("|---5.查看已有图书列表---|")
print("|---0.退出程序---|")

while True:
    number = int(input("你输入的号码为:\n"))

    if number == 1:
        new_user_register()
    elif number == 2:
        print(old_user_login())
    elif number == 3:
        add_book()
    elif number == 4:
        book_name = input("请输入要查询的书名：")
        show_any_book(book_name)
    elif number == 5:
        show_book_set()
    elif number == 0:
        print("感谢使用本图书馆系统，再见！")
        break
    else:
        print("无效输入，请重新输入！")

