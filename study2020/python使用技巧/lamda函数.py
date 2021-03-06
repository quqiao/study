# -*- coding: utf-8 -*-
__author__ = 'quqiao'

"""
匿名函数lamda：是指一类无需定义标识符（函数名）的函数或子程序
lamda匿名函数可以接收任意多个参数（包括可选参数）并且返回单个表达式的值，主要是多个输入一个输出
lamda匿名函数格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式，其实lamda返回值是一个函数地址
                  也就是函数对象
"""
a = lambda x, y, z: (x+8)*y-z
print(a(1, 2, 3))