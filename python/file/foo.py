#coding=utf-8
'''
Created on 2016年5月27日

@author: quqiao
'''


#打开一个文件
fo=open("foo.txt","r+");
str=fo.read(10);
print "读取的字符串：",str

#查找当前位置
position=fo.tell();
print "当前文件位置：",position

#把指针再次重新定位到文件开头
position=fo.seek(0,0);
str=fo.read(20);
print "重新读取字符串：",str

#关闭文件
fo.close()




