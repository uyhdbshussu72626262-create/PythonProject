
# 面向对象的公共图书管理系统
import random

user_data = {}
book_set = {}
book_manager_set={}

class Library_director:

    def __init__(self,name="" ,duty=""):
        self.name = name
        self.duty = duty

    def director_duty(self):
        book_manager_name=input("输入图书管理员姓名为:")
        print(f"这个图书管理员在工作中犯了严重错误或者违背纪律")
        print(f"将马上开除这位图书管理员")
        if book_manager_name in book_manager_set:
            del book_manager_set[book_manager_name]
            print(f"图书管理员{book_manager_name}已从管理员列表删除")
class Book_manager:

    def __init__(self,name="",id="",password=""):
        self.name = name
        self.id = id
        self.password = password

    def new_book_manager_register(self):
        book_manager_name = input("管理员姓名:")
        book_manager_ID = input("输入管理员编号为:")
        manager_password = input("管理员密码:")
        
        book_manager_set[book_manager_name] = {
            "管理员编号": book_manager_ID,
            "管理员密码": manager_password
        }
        print(f"注册成为图书管理员成功")

    def generate_unique_book_id(self):
        while True:
            book_id = ''.join(random.choices('0123456789', k=10))  
            # 生成10位随机数字
            if book_id not in [book['编号'] for book in book_set.values()]:  
                # 确保编号唯一
                return book_id    

    def manager_add_book(self): 
        name = input("请输入你的姓名")
        password = input("请输入管理员密码")
        if name in book_manager_set and book_manager_set[name]["管理员密码"] == password:
            book_name = input("书本名称为:")
            if book_name in book_set:
                print("本书已被存入")
            else:
                book_id = self.generate_unique_book_id()
                author = input("作者为:")
                publish_date = input("出版时间为:")
                book_type = input("书籍类型:")

                book_set[book_name] = {
                    "图书编号": book_id,
                    "作者": author,
                    "出版时间": publish_date,
                    "书籍类型": book_type
                }
                print(f"加入《{book_name}》成功")

    def manager_delete_book(self):
        name = input("请输入你的姓名")
        password = input("请输入管理员密码")
        if name in book_manager_set and book_manager_set[name]["管理员密码"] == password:
            book_name=input("请输入你要删除的图书的书名")
            if book_name in book_set:
                del book_set[book_name]
                print(f"图书《{book_name}》已被删除")
            else:
                print(f"没有这本要删除的图书,\n"
                    f"请您认真检查是否图书名称输入错误")
    
    #管理员删除列表中的某个用户
    def manager_cancel_user_borrow_right(self):
        name = input("请输入你的姓名")
        password = input("请输入管理员密码")
        if name in book_manager_set and book_manager_set[name]["管理员密码"] == password:
            user_name = input("请输入要删除的用户的名称")
            if user_name in user_data:
                del user_data[user_name]
                print(f"用户--{user_name}--已被删除")
            else:
                print(f"用户不存在无法删除")

class User:

    def __init__(self,name="",id=""):
        self.name = name
        self.id = id

    def new_user_register(self):
        user_name = input("创建用户名为:")
        password = input("(请确认环境是否安全)创建密码为:")
        user_data[user_name] = password
        print(f"用户 {user_name} 注册成功！")

    def old_user_login(self):
        return "欢迎再次光临本馆，请输入指令进入其他环节"
class Show:
    def show_any_book(self,book_name):
        if book_name in book_set:
            info = book_set[book_name]
            print(f"书名：{book_name}")
            print(f"作者：{info['作者']}")
            print(f"出版时间：{info['出版时间']}")
        else:
            print("抱歉，本馆还没有这本书")

    def show_book_set(self):
        print(f"{book_set}")

    def show_user_set(self):
        print(f"{user_data}")

    def show_manager_set(self):
        print(f"{book_manager_set}")

def print_menu():
    print("欢迎进入本图书馆，\n")
    print("本图书馆书籍丰富，环境良好，\n")
    print("是个学习放松的好地方.\n")
    print("新用户请根据提示指令注册为本图书馆的用户")
    #指令列表
    print("|---1.注册新用户---|")
    print("|---2.注册成为图书管理员---|")
    print("|---3.老用户登录---|")
    print("|---4.图书管理员添加图书---|")
    print("|---5.图书管理员删除图书---|")
    print("|---6.图书管理员删除用户---|")
    print("|---7.查看某本图书---|")
    print("|---8.查看已有图书列表---|")
    print("|---9.查看用户列表---|")
    print("|---10.查看图书管理员列表---|")
    print("|---11.馆长开除管理员---|")
    print("|---0.退出程序---|")

def main():
    director = Library_director()
    manager = Book_manager()
    user = User()
    show = Show()


    while True:
        print_menu()
        #潜在异常的处理
        try:
            number = int(input("你输入的号码为:\n"))
        except ValueError:
            print(f"无效数字请重试")
            continue

        if number == 1:
            user.new_user_register()  
        elif number == 2:
            manager.new_book_manager_register()
        elif number == 3:
            print(user.old_user_login())
        elif number == 4:
            manager.manager_add_book()
        elif number == 5:
            manager.manager_delete_book()
        elif number == 6:
            manager.manager_cancel_user_borrow_right()
        elif number == 7:
            book_name = input("请输入要查询的书名：")
            show.show_any_book(book_name)
        elif number == 8:
            show.show_book_set()
        elif number == 9:
            show.show_user_set()
        elif number == 10:
            show.show_manager_set()
        elif number == 11:
            director.director_duty()
        elif number == 0:
            print("感谢使用本图书馆系统，再见！")
            break
        else:
            print("无效输入，请重新输入！")
if __name__=='__main__':
    main()
