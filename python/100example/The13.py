#coding=utf-8
'''
Created on 2016年5月11日

@author: quqiao
'''

for n in range(100,999):
    j=n/100
    k=n/10%10
    l=n%10
    if n==j**3+k**3+l**3:
        print n
    
    