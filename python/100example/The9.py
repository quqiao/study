#coding=utf-8
'''
Created on 2016年5月9日

@author: quqiao
'''
l1=[]
i=2
while(i<100):
    j=2
    while(j<=i/j):
        if not(i%j):break
        j=j+1
    if (j>i/j):print i,"是素数"
    i=i+1
    l1.append(i)
    
print "Good bye!"
print sum(l1)


