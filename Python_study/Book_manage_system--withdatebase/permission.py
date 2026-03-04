# permission.py
# 权限控制模块（不修改主程序，仅导入即可生效）

from functools import wraps

# ----------------------------
# 功能码权限映射
# ----------------------------

PERMISSION_MAP = {
    1: "all",      # 用户注册
    2: "all",      # 管理员注册
    3: "all",      # 用户登录
    4: "all",      # 管理员登录
    5: "admin",    # 添加图书
    6: "admin",    # 删除图书
    7: "admin",    # 删除用户
    8: "both",     # 查询单本书
    9: "both",     # 查看所有图书
    10: "admin",   # 查看用户列表
    11: "admin",   # 查看管理员列表
}


# ----------------------------
# 权限管理器
# ----------------------------

class PermissionManager:

    current_role = None   # 当前身份

    @classmethod
    def set_role(cls, role):
        cls.current_role = role

    @classmethod
    def check_permission(cls, code):
        required = PERMISSION_MAP.get(code)

        if required == "all":
            return True

        if required == "both":
            return cls.current_role in ("admin", "user")

        if required == "admin":
            return cls.current_role == "admin"

        return False


# ----------------------------
# 装饰器（拦截 main）
# ----------------------------

def permission_guard(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        import builtins

        original_input = builtins.input

        def secure_input(prompt=""):
            value = original_input(prompt)

            # 只拦截功能选择输入
            if "选择功能" in prompt or "功能号" in prompt:
                try:
                    code = int(value)
                except ValueError:
                    return value

                if not PermissionManager.check_permission(code):
                    print("权限不足，无法执行该操作")
                    return "-1"  # 强制无效菜单

            return value

        builtins.input = secure_input

        result = func(*args, **kwargs)

        builtins.input = original_input
        return result

    return wrapper