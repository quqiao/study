#coding=utf-8
#from day4.reflect import userspance

'''
#系统异常
try:
    data = raw_input('请输入地址')
    array = data.split('/')
    userspance = __import__('backend.'+array[0])
    model = getattr(userspance, array[0])
    func = getattr(model,array[1])
    func()
except ImportError,e:
    print 1,e
    print '跳转到自定义的404'
except AttributeError,e:
    print 2,e
    print '跳转到自动以的404'
except Exception,e:
    print 3,e
    print '跳转到自定义的404'
else:
    print '没有出错'
    
finally:
    print '无论异常与否，都会执行！'
'''

'''
#自定义异常
class MyException(Exception):
    def __init__(self,msg):
        self.error = msg
    def __str__(self,*args,**kargs):
        #return self.error
        return '该对象是MyException类的实例化的一个例子'
    
#obj = MyException('错误')
#print obj

raise MyException('自定义错误')
'''


#主动触发，raise
def Validate(name,pwd):
    if name == 'alex' and pwd == '123':
        return True
    else:
        return False
    
res = Validate('alex', '456')

try:
    res = Validate('alex', '456')
    if res:
        print '登录成功'
    else:
        #print '记录日志到数据库'
        #print '登录失败'
        raise Exception('登录失败')
except Exception,e:
    print '记录日志到数据库'
    print e



    