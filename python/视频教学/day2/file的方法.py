#coding=utf-8
'''
Created on 2016年12月27日

@author: quqiao
'''

# f.closed 标志符，false：文件被打开，true没有被打开
# f.encoding 字符集      默认None:ascii码
# f.flush() 强制写入
# f.newlines() 
# f.next() 迭代
# f.errors()
# f.read() 字符串
# f.readlines()  列表形式
# f.seek() 位置
# f.tell() 告诉所在位置
# f.truncate() 截断
# f.writelines() 写入多行
# f.xreadlines() 迭代器，一行一行的读，不占内存，特别快

f = file('encode.txt','w')

f.write(u'吉泽步'.encode('utf-8'))

f.close()