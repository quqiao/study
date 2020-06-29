#coding=utf-8

'''
a='123456'

b='abcdefg'

c=a+b

print ','.join(c)


d=['1','a','b']
print ''.join(d)
'''
'''
for i in range(65,91):
    print chr(i)
'''
'''
def test(b):
    a = eval(b)
    return a

a='{"name":"heh","age":6}'
print test(a)
'''

def dedao(m,n):
    #y=m
    z=m.get(n)
    print z 
    #return z

dedao({"name":"heh","age":6},'name')

