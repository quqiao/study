"""
面向对象
对象 = 属性 + 行为（方法）
类就是对象

三大特性
封装: 把乱七八糟的数据放在列表里面，这个是数据层的封装，
     把常用的代码段打包成函数，这个也是一种封装，这个是语句层的封装
     对象就是两种合一，更高级的封装
多态：一个对象，不同的实例
     python中是没有真正的多态
继承：className，用于指定类
     BaseClassList,用于指定要继承的基类，可以有多个，类名都是用逗号隔开
"""

# class Trike():
#     # 属性
#     color = 'green'
#     weight = 10
#     legs = 4
#     mouth = '大嘴'
#
#     # 方法
#     def climb(self):
#         print("我正在努力往前爬......")
#     def run(self):
#         print("我正在飞快的往前跑......")
#     def bite(self):
#         print("咬死你，咬死你，咬死你......")
#     def eat(self):
#         print("我正在吃肉肉......")
# a = Trike()  # 实例化，把图纸变成真正的房子
# a.bite()
# b = Trike()
# b.bite()

"""继承示例"""
class Fruit:
    color = "绿色"

    def harvest(self, color):
        print("水果是:" + color + "的！")
        print("水果已经收获......")
        print("水果原来是:" + Fruit.color + "的！")

class Apple(Fruit):
    color = "红色"

    def __init__(self):
        print("我是苹果")

class Banana(Fruit):
    color = "黄色"

    def __init__(self):
        print("我是香蕉")

banana = Banana()
banana.harvest(banana.color)