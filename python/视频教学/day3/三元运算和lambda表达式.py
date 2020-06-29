#coding=utf-8
'''
temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print temp

result = 'gt' if 1>3 else 'lt'  #三元运算
print result
'''

'''
temp = lambda x,y,z:x+y+z    #lambda匿名函数，没有名，只能调用一次，简单不经常调用    

print temp(4,4,10)
'''


print map(lambda x:x*2,range(10))
