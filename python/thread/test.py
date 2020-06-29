#!/usr/bin/python

import encrypt
setEnv(1);
token = "72465872a0ff482784a8985615792f4f"
test = "version=1.0.0&cityId=51010000&deviceNo=0d8c6153aa27470ca9b6aa481cb343fa&deviceType=2&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":1}"

for i in range(0, 100, 1):
    print '#'*40, 'test: ', i, '#'*40, '\n'

    code = encrypt.initSdk(token)

    if code == 0x1008:
        deskey = encrypt.getToken()
        signature = encrypt.signature(test, deskey)
        strEncrypt = encrypt.encrypt(test, deskey)
        print strEncrypt
        strDencrypt = encrypt.dencrypt(strEncrypt, deskey)
        print strDencrypt
    else:
        print "error:"
