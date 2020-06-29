#coding=utf-8
'''
Created on 2016年5月10日

@author: quqiao
'''

for num in range(1,100):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            #print '%d等于%d*%d'%(num,i,j)
            break
    else:
        print num,"是一个质数"
          
