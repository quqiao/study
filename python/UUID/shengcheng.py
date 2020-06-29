#coding=utf-8
'''
Created on 2016年6月22日

@author: quqiao
'''

import uuid

print uuid.uuid1()  #从硬件地址和时间生成
print uuid.uuid3(uuid.NAMESPACE_DNS, 'testme')  #从md5算法生成
print uuid.uuid4()  #随机生成
print uuid.uuid5(uuid.NAMESPACE_DNS, 'testme')  #从SHA-1算法生成