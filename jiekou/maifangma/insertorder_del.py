#coding=utf-8
'''
Created on 2016年8月30日

@author: quqiao
'''


import pycurl
import urllib
import StringIO
import encrypt
import time




def PostData(curl,url,data):
    head = ["Accept:*/*"
            ,"User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (sKHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11"
            ,'Accept:*/*' 
            ,'Content-Type:application/x-www-form-urlencoded',  
            ]
    buf = StringIO.StringIO()
    curl.setopt(pycurl.SSL_VERIFYPEER,False)
    curl.setopt(pycurl.HTTPHEADER,head)
    curl.setopt(pycurl.POSTFIELDS,urllib.urlencode(data))
    curl.setopt(pycurl.WRITEFUNCTION,buf.write)
    curl.setopt(pycurl.URL,url)
    curl.setopt(pycurl.CUSTOMREQUEST,"POST")
    curl.perform()
    the_page=buf.getvalue()
    buf.close()
    return the_page

userArray      = []
ticketIDAarray = []
account=["18008062016","17713543052"]

for i in account:
    print i

userInfo = {"version":"1.0.0",
                    "deviceNo":"72465872a0ff482784a8985615792f4f",
                    "deviceType":"2",
                    "cityId":"5101000",
                    "data":{"account":i,"password":"123456","type":"2"},
                    "ticketId":"null"}   

userArray.append(userInfo)
time.sleep(10)


# 初始化用户数据，包含用户名 密码 ID
'''
def initUsers(userArr):
    for i in range(13611111111,13611112111):
        userInfo = {"version":"1.0.0",
                    "deviceNo":"72465872a0ff482784a8985615792f4f",
                    "deviceType":"2",
                    "cityId":"5101000",
                    "data":{"account":str(i),"password":"123456","type":"2"},
                    "ticketId":"null"} 
        userArr.append(userInfo)
        print len(userArr) 

'''

# 登录一个用户，并获取TICKETID
def loginByUsernName(userInfo,ticketId):
    #
    userInfo['account']
    #loggin
    token      = "72465872a0ff482784a8985615792f4f"
    test_login = "http://test.passport.maifangma.com/login"
    c = pycurl.Curl()
    encrypt.initSdk(token)
    deskey     = encrypt.getToken()
    signature  = encrypt.signature(userInfo, deskey)
    strencrypt = encrypt.encrypt("{\"account\":\"1800806216\",\"password\":\"111111\",\"type\":\"2\"}",deskey)
    data1={"sign":signature,
               "version":"1.0.0",
               "deviceNo":"72465872a0ff482784a8985615792f4f",
               "deviceType":"2",
               "cityId":"51010000" , 
               "data": strencrypt}
    print "%s" %PostData(c, test_login, data1)
    
    
    
    #set ticket id
    ticketId=userInfo['ticketId']
    return ticketId
time.sleep(10)  
#登录全部用户   

def loginAllUsers(userArray):
    for user in userArray:
        loginByUsernName(user)
        print user
        
        
'''  
def login(dict1,signature2):
    token      = "72465872a0ff482784a8985615792f4f"
    test_login = "http://test.passport.maifangma.com/login"
    test_data3 = {"version":"1.0.0",
                  "deviceNo":"72465872a0ff482784a8985615792f4f",
                  "deviceType":"2",
                  "cityId":"5101000",
                  "data":{"account":a,"password":"123456","type":"2"}
                  }
    c = pycurl.Curl()
    encrypt.initSdk(token)
    deskey     = encrypt.getToken()
    signature  = encrypt.signature(test_data3, deskey)
    strencrypt = encrypt.encrypt("{\"account\":\"1800806216\",\"password\":\"111111\",\"type\":\"2\"}",deskey)
    data1={"sign":signature,
               "version":"1.0.0",
               "deviceNo":"72465872a0ff482784a8985615792f4f",
               "deviceType":"2",
               "cityId":"51010000" , 
               "data": strencrypt}
    print "%s" %PostData(c, test_login, data1)
    data2=demjson.decode(PostData(c,test_login,data1))
    data3=data2.get('data')
    dencryptData = encrypt.dencrypt(data3,deskey)
    dict1=eval(dencryptData)
    print dict1
    test_data2= "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000}"
    signature2=encrypt.signature(test_data2, deskey)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    return signature2
'''
   
   
def insertorderAllUsers(ticketIDAarray):
    for user in ticketIDAarray:
        insertorder(user)
        print user 
   
def insertorder(ticketId,signature2):
    c=pycurl.Curl()
    test_insertorder="http://platforms.maifangma.com/steward/insertorder"
    data_insertorder={"sign":signature2,
            "version":"1.0.0",
            "deviceNo":"72465872a0ff482784a8985615792f4f",
            "deviceType":"2",
            "cityId":"51010000" , 
            "ticketId": ticketId,
            "housesId": "",
            "phone": "",
            "sex": "",
            "orderDate": "",
            "orderUserName": "",
            "housekeeperId": ""}
    print "%s" %PostData(c, test_insertorder, data_insertorder)
time.sleep(10)
    
    

def del1AllUsers(ticketIDAarray):
    for user in ticketIDAarray:
        del1(user)
        print user
        

def del1(ticketId,signature2):
    c=pycurl.Curl()
    test_del="http://platforms.maifangma.com/orders/del"
    data_del={"sign":signature2,
            "version":"1.0.0",
            "deviceNo":"72465872a0ff482784a8985615792f4f",
            "deviceType":"2",
            "cityId":"51010000" , 
            "ticketId":ticketId,
            "id": ""}
    print "%s" %PostData(c, test_del, data_del)

    
    
        
    