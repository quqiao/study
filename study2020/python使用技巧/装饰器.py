"""
装饰器（decorators）: python 重要组成部分
                     作用：是修改其他函数的功能函数
"""

"""一切皆对象"""
# def hi(name = 'chaxun'):
#     return "hi" + name
# # print(hi())  # 输出：'hi chaxun'
# greet = hi  # 将一个函数赋值给一个变量，这里没有使用小括号，我们不是在调用hi函数，而是将它放在greet变量里头
# # print(greet())
# del hi  # 删掉旧的hi函数
# # print(hi())
# print(greet())

"""在函数中定义函数
   可以在函数中定义另外的函数，也就是说，我们可以创建嵌套的函数
"""
# def hi():
#     print("now you are in hi() function")
#     def greet():
#         return "now you are in greet() function"
#     def welcome():
#         return "now you are in welcome() function"
#     print(greet())
#     print(welcome())
#     print("now you are back in the hi() function")
#
# hi()
# greet()  # 无法调用函数中的定义的函数

"""从函数中返回函数"""
# def hi(name = "yahoo"):
#     def greet():
#         return "now you are in the greet() function"
#     def welcome():
#         return "now you are in the welcome() function"
#     if name == "yahoo":
#         return greet
#     else:
#         return welcome
# a = hi()
# print(a)
# print(a())

"""将函数作为参数传给另一个函数"""
# def hi():
#     return "hi yahoo!"
# def doSomethingBeforeHi(func):
#     print("I am doing some boring work before executing hi()")
#     print(func())
# doSomethingBeforeHi(hi)

"""第一个装饰器"""
# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#         a_func()
#         print("I am doing some boring work after executing a_func()")
#     return wrapTheFunction
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
# # a_function_requiring_decoration()
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# a_function_requiring_decoration()

"""导入functools"""
# from functools import wraps
# def a_new_decorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#         a_func()
#         print("I am doing some boring work after executing a_func()")
#     return wrapTheFunction
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey yo! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
# a = a_function_requiring_decoration()
# print(a)

# import logging
# def use_logging(func):
#     def wrapper():
#         logging.warning("%s is running" % func.__name__)
#         return func()
#     return wrapper
# @use_logging
# def foo():
#     print("i am foo")
# foo()