"""
条件控制和循环的学习
"""

"""输入名字判断情况"""
# name = input("请输入名字：")
#
# if name == "Monster":
#     print("你好！Monster")
# else:
#     print("你好,", name)

"""登录情况验证, user=admin, password=123456"""
for i in range(3):
    user = input("请输入用户名：")
    password = input("请输入密码：")
    if (user == "" or password == ""):
        print("用户名或者密码为空")
    elif (user == "admin" and password != "123456"):
        print("密码错误")
    elif (user != "admin" and password == "123456"):
        print("用户名错误")
    elif (user != "admin" and password != "123456"):
        print("用户名和密码都错误！")
    else:
        print("登录成功")

