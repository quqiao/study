#coding=utf-8


#参数  def Fun(arg, *args,**kargs):
#默认参数  
#可变参数 
#返回值 return 'success'


'''
def Foo():
    Bar()
    print "老苟去砍柴"
    
def Bar():
    print "李阳去收租"
    #调用其他900008个函数
'''
    
#函数 ,作用：封装功能， 分解功能
'''
def foo(name,action='砍柴',where='北京'):  #aciton=砍柴 为默认函数，默认函数放后边
    print name ,'去',action,where
    
    
foo('liyang','beijing')
foo('laogou','bb')
foo('alex',where='上海')
foo('zhu','四川','dushu')
foo('zhutou',where='四川',action='xiezuo')
'''

'''
def login(username):
    if username == 'alex':
        return 'successful'   #返回值
    else:
        return 'fail'  #返回值
        
def detail(user):
    print user,"余额"
        
if __name__=='__main__':
    user=raw_input("请输入用户名：")
    
    res=login(user)#检查用户是否合法
    if res =='successful':
        detail(user)
    else:
        print "错误"
'''

def show(*arg):   #*arg可变长度，有多少传多少
    for item in arg:
        #各种炫酷效果
        print item
show('liyang','ss','MT','fs')

'''
def show2(arg1=1,arg2):
    print arg1,arg2
'''



'''
def show1(**kargs):
    for item in kargs.items():
        print item
        
show1(name='liyang',age='20',zhiye='IT')
'''

    
