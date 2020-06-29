#coding=utf-8
'''
Created on 2016年12月27日

@author: quqiao
'''
# r以只读的模式打开文件
# w以只写的模式打开文件
# a以追加的模式打开文件
# r+b以读写的模式打开
# w+b以写读的模式打开  清空再写，读
# a+b以追加及读的模式打开   b:二进制模式处理文件，windows上用

#f= file('test.txt','r')
#f.readline()

#f= file('test1.txt','w')
#f.write('haha')

f= file('test1.txt','a')
f.write('hehe')
f.write('heihei')
f.flush()  #强制写入文件


f.close() 