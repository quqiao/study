#coding=utf-8
'''
Created on 2017年1月10日

@author: quqiao
'''
#dict:
#查找和插入的速度极快，不会随着key的增加而增加
#需要占用大量的内存，内存浪费多
#key不可变
#默认无序

#list：
#查找和插入的时间随着元素的增加而增加
#占用空间小，浪费内存少
#通过下标查询
#有序

#set集合
#特点：无序，元素不重复
#功能：关系测试，去重

name_set = {1,2,3,4,5,5}
#print name_set

#添加相同的不再显示，不同的显示
name_set.add(1)
name_set.add(6)
#print name_set


x={1,2,3,4}
y={3,4,5,6}
print x&y  #类似a.intersection(b)
print x|y  #类似a.union(b)
print x-y  #类似a.difference(b)
print x^y  #类似a.symmetric_difference(b)
#a.issubset(b)  a是b的子集
z={1,2,4}
v={1,2,3,4}
print z.issubset(v)
print v.issuperset(z)
#a.issuperset(b) a是否包含b

