#coding=utf-8
'''
Created on 2016年5月11日

@author: quqiao
'''
'''
a='cfcfcfccfffcfcfffcfcfcfcfcf'

b=a.replace('ccfff', '!')
#print b

c=b.replace('fff','f!')
#print c

d=c.split('!')
#print d

e1=d[0]
#print e1
g1=e1.count('cf')
#print g1

e2=d[1]
#print e2
g2=e2.count('cf')

e3=d[2]
#print e3
g3=e3.count('cf')

x=[]
x.append(g1)
x.append(g2)
x.append(g3)
#print x

y=max(x)
print y
'''

a=[1,2,3,4,5]
b=a[1:-1]
c=a[-5:-1]
print b
print c
