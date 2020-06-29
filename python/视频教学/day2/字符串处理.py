#coding=utf-8
'''
Created on 2017年1月3日

@author: quqiao
'''

# S.find(substring,[start[end]])  可指范围查找子串，返回索引值，否则返回-1
# S.rfind(substring,[start[end]]) 反向查找
# S.index(substring,[start[end]]) 同find,只是找不到产生ValueError异常
# S.rindex(substring,[start[end]]) 同上反向查找
# S.count(substring,[start[end]]) 返回找到子串的个数
# S.lowercase() 所有字符串变为小写
# S.capitalize() 首字母大写
# S.lower 转小写
# S.upper 转大写
# S.swapcase()大小写互换
# S.split(str,'')将string转list，以空格切分
# S.join(list,'')将list转string，以空格连接
# S.startswith() 以开头
# S.endswith()  以结尾


#处理字符串的内置函数
#len(str) 字符串长度
#cmp("my friend",str)字符串比较。第一个大，返回1
#max['abcxyz] 寻找字符串中最大字符
#min['abcxyz']寻找字符串中最小字符



msg="what's your company's name?"

print msg.find('name')
print msg.rfind('name')
print msg.index('name')
print msg.capitalize()
print msg.upper()
print msg.split()
msg1=msg.split()
print '|'.join(msg1)

a=['a','l','e','x']
b='a'
b+='l'
b+='e'
b+='x'
print b
print ''.join(a)

x='A'
y='B'
print cmp(x, y) #根据ascii码判断
x1='Abc'
y1='B1'
print cmp(x1,y1)



