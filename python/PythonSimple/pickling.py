#coding=utf-8
'''
Created on 2016年4月21日

@author: quqiao
'''

import cPickle as p

shoplistfile = 'shoplist.data'
#the name of the file where we will store the object

shoplist = ['apple','mango','carrot']

#Write to the file
f = file(shoplistfile,'w')
p.dump(shoplist,f)#dump the object to a file
f.close()

#del shoplist #remove the shoplist

#Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist
