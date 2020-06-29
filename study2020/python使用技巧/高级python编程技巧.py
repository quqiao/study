# -*- coding: utf-8 -*-
__author__ = 'quqiao'

"""1.同时给多个变量赋值"""
# a = 1
# b = "ab"
# c = [1, 2, 3]
# print(a, b, c)
# d, e, f = 2, "cd", [4, 5, 6]
# print(d, e, f)

"""2.交换两个变量的值"""
# a = 4
# b = 5
# temp = a
# a = b
# b = temp
# print(a, b)
#
# c = 6
# d = 7
# c, d = d, c
# print(c, d)

"""3.序列解包,
   对应的数在不知道有多少个时，可以使用'*'去接收剩余所有的,封装成列表
"""
# student = ["Jerry", 30, "M"]
# name = student[0]
# age = student[1]
# gender = student[2]
# print(name, age, gender)
#
# name1, age1, gender1 = student
# print(name1, age1, gender1)
#
# a, b, *c = 1, 2, 3, 4, 5, 6, 7, 8
# print(a, b, c)
#
# def func():
#     return 1,2,3,4
# a,*b = func()
# print(a, b)

"""4.三目运算符"""
# a = 5
# if a>0:
#     b = a
# else:
#     b = -a
# print(b)
# a = -6
# b = a if a > 0 else -a
# print(b)

"""5.区间判断"""
# score = 76
# if score >80 and score< 90:
#     level = "B"
# elif 70 < score < 80:
#     level = "C"
# print(level)

"""6.判断是否为多个取值之一"""
# level = "A"
# if level == "A" or level == "B" or level == "C":
#     print("pass")
# else:
#     print("fail")
#
# if level in ('A', 'B', 'C'):
#     print("passed")

"""7.判断字典，字符串，列表是否为空
     1)通过求长度
     2)通过元素布尔值判断
"""
# d2 = '1'
# if len(d2)>0:
#     print('not null')
#
# student = []
# if student:
#     print("not null")
# else:
#     print("null")

"""8.判断诸多条件是否至少有一个成立
     关键字 any
"""
# math, english, chinese = 80, 50, 90
# if math < 60 or english < 60 or chinese < 60:
#     print("fail")
# if any([math < 60, english < 60, chinese < 60]):
#     print("F")

"""9.判断诸多条件是否全部成立
     关键字 all
"""
# math, english, chinese = 80, 61, 90
# if math > 60 and english > 60 and chinese > 60:
#     print("pass")
# if all([math > 60, english > 60, chinese > 60]):
#     print("P")

"""10.同时遍历列表的元素和下标"""
# li = ['a', 'b', 'c']
# for i in range(len(li)):
#     print(i, ':', li[i])
#
# for i, item in enumerate(li):  # (0, 'a'), (1, 'b')
#     print(i, ":", li[i])

"""11.从两个列表中生成字典"""
# name = ['a', 'b', 'c']
# age = [20, 30, 40]
# b = dict(zip(name, age))
# print(b)

"""12.匿名函数
      lambda x : express
"""
# li = [1, 2, 3, 'a', 'c', 4]
# res = filter(lambda x: isinstance(x, int), li)
# for i in res:
#     print(i)

"""13.列表推导式
      快速简单的生成一个列表
"""
# li = [i*i for i in range(1, 11) if i % 2 == 0]
# print(li)

"""14.生成器
      保存元素生成的算法
      通过next() 一步一步的出来
"""
# gen = (i for i in range(1, 11))
# print(next(gen))

"""15.装饰器"""








