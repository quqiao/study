#coding=utf-8
'''
Created on 2017年1月4日

@author: quqiao
'''

a=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,1,2,3,4,5]

pos=0
for i in range(a.count(2)):
    if pos==0:
        pos = a.index(2)
    else:
        pos = a.index(2, pos+1)
    print pos