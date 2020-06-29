#coding=utf-8

import hashlib
#MD5加密
hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
print hash.digest()