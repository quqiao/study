#coding=utf-8
'''
Created on 2016年5月5日

@author: quqiao
'''

#example1

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i==j)and(i==k)and(j==k):
                print i,j,k
