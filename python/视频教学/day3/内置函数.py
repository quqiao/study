#coding=utf-8

#help()提示帮助信息
'''
a=[]
print help(a)
'''

#dir()目录
'''
b=[]
print dir(b)
'''

#vars()
'''
c=[]
print vars(c)
'''

#type() 类型
'''
d=[]
print type(d)
'''

#reload() 重载一次导入

#id()  打印ID号
'''
t1=123
t2=456

print id(t1)
print id(t2)
'''

#abs()绝对值
#print abs(-9)

#bool() 布尔类型
#print bool(-1)

#divmod() 除，商
#print divmod(10, 3)
#print divmod(9,3)

#max() min() sum() 最大值，最小值，求和
#print max([11,22,33,44,55,66])
#print min([11,22,33,44,55,66])
#print sum([11,22,33,44,55,66])

#pow() 指数
#print pow(10,2)

#all() 迭代判断都是真才为真
#print all([1,2,3,4,1])

#any 迭代判断，都为0才是假
#print any([0,0,0,0])

#chr()ASCII码对应
#print chr(66)
#print chr(67)
#print chr(68)

#ord()
#print ord('A')

#hex()16进制，oct()8进制，bin()2进制
#print hex(10)
#print oct(10)
#print bin(10)

'''
li = ['手表','汽车','房']
for item in li:
    print item
    
for item in enumerate(li,1):
    print item[0],item[1]
'''

'''
s = 'i am {0},{1}'
print s.format('alex','xxx')
'''

'''
def Function(arg):
    print arg
Function('alex')
apply(Function,('aaaa'))
'''

'''
#添加增加后的列表
li = [11,22,33,44,55]
temp = []

for item in li:
    temp.append(item+100)
print temp
'''

'''
#map()所有元素统一操作
def foo(arg):
    return arg+100
li = [11,22,33]
temp = map(lambda arg:arg+100,li)
print temp
'''

'''
#filter()过滤条件
li = [11,22,33]
def foo(arg):
    if arg<22:
        return True
    else:
        return False
temp=filter(foo,li)
print temp
'''

'''
#reduce()累加，累乘，累除
li = [11,22,33,55]
print reduce(lambda x,y:x+y,li)
'''

'''
#zip()
x = [1,2,3]
y = [4,5]
z = [4,5,9]
print zip(x,y,z)
'''

'''
#字符串的加减乘除
a='8*8'
print eval(a)
'''

'''
for k,v in enumerate([1,2,3,4]):
    print k,v
'''