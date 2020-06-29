#coding=utf-8
'''
def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    
re=foo()
for item in re:
    print item
'''

'''
for item in range(5):
    print item
    
for item1 in xrange(10):
    print item1
'''

'''
def AlexReadlines():
    seek = 0
    while True:
        with open('D:/temp.txt','r') as f:
            f.seek(seek)
            data = f.readline()
            if data:
                seek = f.tell()
                yield data
            else:
                return
            
for item in AlexReadlines():
    print item
'''

'''
alist = [1,2,3,4]
def addlist(alist):
    for i in alist:
        yield i+1

for x in addlist(alist):
    print x
'''

'''
def h():
    print 'wen chuan'
    yield 1
    print 'Fighting!'
c=h()
c.next()
'''

'''
def h():
    print 'wen chuan'
    m = yield 5
    print m
    d = yield 12
    print 'we are together!'
c=h()
c.next()
#c.next()
c.send('Fighting!') #yield 5 表达式被赋予了'fighting'
#c.send('jiayou')
'''

'''
def h():
    print 'wen chuan',
    m = yield 5     #fighting!
    print m
    d = yield 12
    print 'we are together!'
c = h()
m = c.next() #m获取了yield 5的参数值5
d = c.send('Fighting!') #d 获取了yield 12的参数值12
print m
print d
print 'we will never forget the date',m,'.',d
'''

def close(self):
    try:
        self.throw(GeneratorExit)
    except(GeneratorExit,StopIteration):
        pass
    else:
        raise RuntimeError("generator ignored GeneratorExit")