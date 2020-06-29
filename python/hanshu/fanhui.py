#coding=utf-8
'''
Created on 2016年5月25日

@author: quqiao
'''



#可写函数说明
def sum(agrs1,agrs2):
    #返回2个参数的和
    total=agrs1+agrs2
    print"函数内：",total
    return total;

#调用sum函数
total=sum(10,20)
print"函数外：",total




total=0 #这是一个全局变量
def sum1(args1,args2):
    total=args1+args2;
    print "局部变量为：",total
    return total;

#调用sum1函数
sum1(100,200);
print "全局变量为：",total

