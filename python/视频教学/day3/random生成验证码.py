#coding=utf-8

import random

#print random.random()  #生成小于1的随机数
#print random.randint(1,6)  #生成随机整数
#print random.randrange(1,10) #生成范围

#temp= random.randint(65,90)
#print chr(temp)

code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
print code

print ''.join(code)  #列表转换为字符串

