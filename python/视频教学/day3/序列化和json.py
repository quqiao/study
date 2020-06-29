#coding=utf-8

#序列化：特殊的二进制加密，序列化和反序列化

'''
#pickle序列化，只能在Python中用，还可以序列化类，对象
import pickle

li = ['alex',11,22,'ok','sb']

dumpsed = pickle.dumps(li)   #序列化
print dumpsed
print type(dumpsed)

loadsed = pickle.loads(dumpsed) #反序列化
print loadsed
print type(loadsed)


#pickle.dump(li, open('xuleihua.txt','w'))  #将序列化后写入文件中

result = pickle.load(open('xuleihua.txt','r'))  #将文件中的反序列化回来
print result
'''

#json  不能语言间的交互，只能序列化常规数据类型（列表，字典等）
import json
name_dic = {'name':'wupeiqi','age':23}
result1 = json.dumps(name_dic)#jason格式
print result1
print type(result1)

#result2 = json.loads(result1)#切换回字典格式
#print result2
#print type(result2)

#json.dump(name_dic,open('json.txt','w'))
#result3 = json.load(open('json.txt','r'))
#print result3


