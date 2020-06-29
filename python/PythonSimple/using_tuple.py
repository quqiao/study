#coding=utf-8
'''
Created on 2015年11月12日

@author: admin
'''
zoo = ('wolf','elephant','penguin')
print 'Number of animals in the zoo is',len(zoo)

new_zoo = ('monkey','dolphin',zoo)
print 'Number of animals in the new zoo is',len(new_zoo)
print 'All animals in new zoo are',new_zoo
print 'Animals brought from old zoo are',new_zoo[2]
print 'Last animal brought from old zoo is',new_zoo[2][2]
