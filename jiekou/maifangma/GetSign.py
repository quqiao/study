#coding=utf-8
'''
Created on 2016年6月22日

@author: quqiao
'''

import encrypt


def encrypt():
    #uuid
    token  ="72465872a0ff482784a8985615792f4f"
    
    params = {"version": "2.0.0", "deviceNo": "ffff", "data": {"type": 1} # step1
    
    temp=toString(params) ==> "version=2.0.0&deviceNo=ffff&data={\"type\": 1}"; // step 2
    
    // step 3 get signaute.
    sign=encrypt.signature();
    
    encrypData = encrypt.encrypt("{\"type\": 1}");
    
    // do post.
    res = post(url, {sign: sign, version: , deviceTo: , data: encryptData}})
    
    // handle res.
    if res.code = 0:
        dencrypData=encrypt.dencrpt(res.data);
    else:
        handle error;
    
    #测试数据
    test="version=1.0.0&deviceNo=DESKTOP-A34KG0E&deviceType=2&cityId=51010000&data={\"account\":\"18008062016\",\"password\":\"123456\",\"type\":2}"


    for i in range(0,100,1):
        print '#'*40,'test:',i,'#'*40,'\n'
    
        code=encrypt.initSdk(token)
    
        if code==0x1008:
            deskey=encrypt.gettoken()
            signature=encrypt.signature(test,deskey)
            strEncypt=encrypt.encrypt(test,deskey)
            strDencypt=encrypt.dencrypt(strEncypt,deskey)
        
        else:
            print "error:"
            
            
            
            

'''def encrypt():
    #uuid
    token  ="72465872a0ff482784a8985615792f4f"
    
    test_data1={"version":"1.0.0","deviceNo":"DESKTOP-A34KG0E","deviceType":"2","cityId":"51010000","data":{"id":"1","houseName":"美城云庭"}} # step1
    
    test=demjson.encode(test_data1)
    #toString(test_data1) ==> "version=2.0.0&deviceNo=ffff&data={\"type\": 1}"; #// step 2
    
    #// step 3 get signaute.
    sign=encrypt.signature(test);
    
    encrypData = encrypt.encrypt(sign);
    
    #// do post.
    res = post(c,url, encrypData)
    
    #// handle res.
    if res.code = 0:
        dencrypData=encrypt.dencrpt(res.data);
    else:
        handle error;
    '''
