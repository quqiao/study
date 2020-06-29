#coding=utf-8
'''
Created on 2016年6月1日

@author: quqiao
'''

a=100.0
b=a/2

for n in range(2,11):
    a +=2*b
    b /=2
    
print "Total of road is %f"%a
print "The tenth is %f meter"%b

    

