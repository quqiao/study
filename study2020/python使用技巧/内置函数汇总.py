# -*- coding: utf-8 -*-
__author__ = 'quqiao'

"""字典排序"""
"""1.利用zip将字典数据转换为元组然后进行排序"""
# ss = {'a': 2, 'b': 1, 'c': 3, 'd': 5, 'e': 9, 'f': 2}
# s = sorted(zip(ss.values(), ss.keys()))
# print(s)
"""2.传递sorted函数key参数"""
# ss = {'a': 2, 'b': 1, 'c': 3, 'd': 5, 'e': 9, 'f': 2}
# s = sorted(ss.items(), key=lambda x: x[1])
# print(s)

"""map
   map()会根据提供的函数对指定序列做映射
   map()函数语法
   map(function, iterable, ...)
   function --- 函数
   iterable --- 一个或多个序列
"""
# def square(x):
#     return x**2
# map(square, [1, 2, 3, 4, 5])
# map(lambda x: x**2, [1, 2, 3, 4, 5])
# map(lambda x, y: x+y, [1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

"""
reduce()函数也是python内置的一个高阶函数
"""
# def add(x, y):
#     return x+y
# reduce(add, [1, 2, 3, 4, 5])
