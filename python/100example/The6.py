#coding=utf-8
'''
Created on 2016年5月9日

@author: quqiao
'''

def fib(n):
    if n==0:
        return [0]
    if n==1:
        return [1,1]
    fibs=[0,1]
    for i in range(1,n):
        fibs.append(fibs[-1]+fibs[-2])
        
    return fibs

print fib(10)
        
    