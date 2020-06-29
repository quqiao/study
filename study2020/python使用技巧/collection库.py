# -*- coding: utf-8 -*-
__author__ = 'quqiao'

"""
collection模块额外提供了几种高级数据类型
namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
deque: 双端排列，可以快速的从另外一侧追加和退出对象
counter: 计数器
ordereddict: 有序字典
defaultdict: 带有默认值得字典
"""

"""
namedtuple():可命名元祖
tuple是一个不可变集合，namedtuple用来构建一个自定义的tuple对象，并且规定了tuple元素的个数，可通过属性而不是
索引来引用tuple的某个元素，我们可以通过nametuple很方便的定义一个数据类型，它具有tuple的不变属性又可以根据属
性来引用
"""
# from collections import namedtuple
# point = namedtuple('point', ['x', 'y'])
# p = point(2, 1)
# print(p)
# print('x=', p.x)
# print('y=', p.y)
# print(isinstance(p, point))
# print(isinstance(p, tuple))

"""
ordereddict: 有序字典
dict中key是无序的，再做迭代时，无法确认key的顺序。
ordereddict是对字典类型的补充，他记住了字典元素的添加顺序
"""
# from collections import OrderedDict
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)
# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)

"""
defaultdict: 默认字典
对字典类型的补充，默认给字典的值设置了一个类型
"""
# from collections import defaultdict
# dict1 = defaultdict(int)
# dict2 = defaultdict(set)
# dict3 = defaultdict(str)
# dict4 = defaultdict(list)
# dict1[2] = 'two'
# print(dict1[1])
# print(dict1[2])
# print(dict2[1])
# print(dict3[1])
# print(dict4[1])

"""
counter: 计数器
counter是对字典类型的补充，用于追踪值出现的次数，
"""
from collections import Counter
c1 = Counter(['1', '2', '2', '4', '5', '4', '4', '2'])
c2 = Counter('assddsseedsassasasassades')
print(c1, c2)
