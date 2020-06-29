#coding=utf-8
'''
Created on 2017年1月6日

@author: quqiao
'''
#字典没有排列，即没有索引


name_info={
           'name':'Jacky',
           'age':20,
           'job':'Engineer',
           'address':'SC',
           'gender':'Male'
           }

#print name_info['name']
#name_info['salary']=3000 #增加
#name_info.pop('job')  #删除
#name_info.popitem() #随机删除

#for i in name_info:  #循环
    #print i  #打印key值
    #print i,name_info[i] #打印key和value值，效率高

#D.items() 将所有的字典项以列表方式返回，这些列表中的每一项都来自于    
#for k,v in name_info.items():
    #print k,v  #打印key和value值，效率低
    
#D.get(key,0) 同dict[key],多了个没有则返回缺省值，0。[]没有则抛异常
#print name_info.get('job')

#D.has_key(key) 有该键返回TRUE,否则返回FALSE
#print name_info.has_key('other')

#D.keys() 返回字典键的列表
#print name_info.keys()

#D.values() 以列表的形式返回字典中的值，返回值的列表中可包含重复元素
#print name_info.values()

#D.setdefault
#name_info.setdefault('stuID',1123)
#print name_info

#D.update() 将字典A和B合起来
#dict1={'didian':'sichuan','chengshi':'chengdu','qu':'chenghua'}
#dict2={'yilou':'huawei','erlou':'zhongxing','sanlou':'lianxiang'}
#dict1.update(dict2)
#print dict1


dict3={'didian':'sichuan','chengshi':'chengdu','qu':'chenghua'}
dict5=dict3
#dict5['didian']='chongqing'
dict3['didian']='beijing'
#print dict3
#print dict5


#浅copy，独立复制
dict8={'didian':'sichuan','chengshi':'chengdu','qu':'chenghua'}
dict9=dict8.copy()
dict8['didian']='hebei'
dict9['didian']='guangdong'
#print dict8
#print dict9


dict10={'didian':'sichuan','chengshi':'chengdu','qu':'chenghua'}
dict10['ex_l']=['Coral','Erion']
dict11=dict10.copy()
dict11['didian']='xianggang'
dict10['ex_l'].append('Wutenglan')
#print dict10
#print dict11

#深copy ，导入import copy
#copy.copy() 浅copy，同上
#copy.deepcopy  深copy
import copy
dict11=copy.deepcopy(dict10)
dict10['ex_l'][2]='longzeluola'
print dict10
print dict11






