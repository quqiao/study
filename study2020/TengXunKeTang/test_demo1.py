"""
Python模拟10086查询功能

涉及的知识点：
条件控制
选择结构
循环结构

"""

"""
例子1
需求：编写python程序，模拟10086自助查询功能系统
     输入1：查询当前余额
     输入2：显示当前流量
     输入3：当前通话时间，单位为分钟
     输入0：退出系统
"""
# print("10086查询功能")
# print("输入1：查询当前余额\n, 输入2：显示当前流量\n, 输入3：当前通话时间，单位为分钟\n, 输入0：退出系统\n")
# while True:
#     info = input("请输入查询：")  # 获取输入内容
#     if info == "1":
#         print("当前余额为999元")
#     elif info == "2":
#         print("当前剩余流量为5G")
#     elif info == "3":
#         print("当前剩余的通话时间为189分钟")
#     elif info == "0":
#         print("退出查询系统")
#         break

"""
例子2：
猜数字游戏：随机输入一个数字（0-10）,然后再进行

"""
# import random
# print("----请输入0-10的数字---")
# number_random = random.randint(0, 10)
# print(number_random)
# # 循环直到猜出为止
# while True:
#     number = int(input("请输入数字："))
#     if number != number_random and number > number_random:
#         print("输入错误,输入过大，请重试")
#     elif number != number_random and number < number_random:
#         print("输入错误，输入过小，请重试")
#     elif number == number_random:
#         print("输入正确！！！")
#         print("-----游戏退出-----")
#         break
#     elif number > 10:
#         print("用户自动退出")
#         break


# 循环三次，三次完成后停止
import random
print("----请输入0-10的数字---")
number_random = random.randint(0, 10)
print(number_random)
for i in range(4):
    number = int(input("请输入数字："))
    if i < 3:
        if number != number_random and number > number_random:
            print("输入错误,输入过大，请重试")
            print("你还有%d次机会" % (2-i))
        elif number != number_random and number < number_random:
            print("输入错误，输入过小，请重试")
            print("你还有%d次机会" % (2-i))
        elif number == number_random:
            print("输入正确！！！")
            print("-----游戏退出-----")
            break
    else:
        print("你的机会已用完")






