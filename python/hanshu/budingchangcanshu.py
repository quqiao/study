#coding=utf-8
'''
Created on 2016年5月24日

@author: quqiao
'''

#可写函数说明
def printinfo(arg1,*vartuple):
    
    print"输出："
    print arg1
    for var in vartuple:
        print var
    return;

#调用printinfo函数
printinfo(10)
printinfo(10,20,30,40,50,60,70,80,90,100)