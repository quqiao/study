#coding=utf-8
'''
Created on 2016年7月25日

@author: quqiao
'''

from locust import HttpLocust, TaskSet, task
import encrypt
import demjson

class UserTasks(TaskSet):
    token  = "72465872a0ff482784a8985615792f4f"
    desKey = ""
    test_data = "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}"
    res = {}
    def on_start(self):
        self.token  = "72465872a0ff482784a8985615792f4f"
        #desKey = ""
        self.test_data = "version=1.0.0&deviceNo=72465872a0ff482784a8985615792f4f&deviceType=2&cityId=51010000&data={\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}"
        encrypt.initSdk(self.token)
        self.deskey = encrypt.getToken()
       
    @task
    def login(self):
        # encrypt.initSdk(token)
        # deskey=encrypt.getToken()
        signature  = encrypt.signature(self.test_data, self.deskey)
        strencrypt = encrypt.encrypt("{\"account\":\"admin\",\"password\":\"123456\",\"type\":\"1\"}",self.deskey)
        data = {"sign":signature,
                 "version":"1.0.0",
                 "deviceNo":"72465872a0ff482784a8985615792f4f",
                 "deviceType":"2",
                 "cityId":"51010000" , 
                 "data": strencrypt}
        self.res = self.client.post("http://test.passport.maifangma.com/login",data,catch_response=True)
        self.assertResult()
        #self.decodeData()
      
    def decodeData(self):
        resObj = demjson.decode(self.res.content)
        data   = resObj.get('data')
        dencryptData = encrypt.dencrypt(data,self.deskey)
        print dencryptData
        return dencryptData
    
    def assertResult(self):
        resObj = demjson.decode(self.res.content)
        print "yinyou ",resObj.get('code')
        if self.res.status_code != 200:
            self.res.failure("status code error")
        elif resObj.get('code') != 0:
            print 'yinyou',resObj.get('data')
            self.res.failure("msg code error")
        else:
            self.res.success()
            
        
class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://test.passport.maifangma.com/"
    min_wait = 0
    max_wait = 0
    task_set = UserTasks