#coding=utf-8
'''
Created on 2016年7月25日

@author: quqiao
'''

from locust import HttpLocust,TaskSet, task
import encrypt
import demjson





class UserTasks(TaskSet):
    # for HTTP request
    token     = '72465872a0ff482784a8985615792f4f'
    desKey    = ''
    res       = {}
    host      = 'http://test.passport.maifangma.com'
    port      = '/login'
    
    # public arguments
    version    = '1.0.0'
    deviceNo   = token
    deviceType = '2'
    cityId     = '51010000'
    ticketId   = ''
    fileStreams= ''
    openid     = ''
    
    pubArgs = {
        'version'    : version ,
        'deviceNo'   : deviceNo,
        'deviceType' : deviceType,
        'cityId'     : cityId,
        'ticketId'   : ticketId,
        'fileStreams': fileStreams,
        'openid'     : openid,
        'data'       : ''
    }

    # private arguments
    data = {
        'account'    : 'admin',
        'password'   : '123456',
        'type'       : '1'
    }
    
    # post data string 
    postStr = ''

    def createPostDataString(self):
        postDataString = ''
        dataStr = '{'
        index = 0
        for (k,v) in self.data.items():
            dataStr =  dataStr + '\"' + k + '\"'+':'+'\"' + v + '\"'
            if index < len(self.data)-1 :
                dataStr =  dataStr +','
            index   = index + 1
        dataStr =  dataStr + '}'
        self.pubArgs['data'] = dataStr
        index = 0
        for (k,v) in self.pubArgs.items():
            if v != '':
                postDataString = postDataString+k+'='+v
                if index < len(self.pubArgs) - 2 :
                    postDataString = postDataString +'&'
            index = index + 1
        return postDataString


    def decodeData(self):
        resObj = demjson.decode(self.res.content)
        data   = resObj.get('data')
        dencryptData = encrypt.dencrypt(data,self.deskey)
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
             
    def on_start(self):
        encrypt.initSdk(self.token)
        self.deskey    = encrypt.getToken()
        self.postStr   = self.createPostDataString()
       
    @task
    def login(self):
        print self.postStr
        signature = encrypt.signature(self.postStr, self.deskey)
        strencrypt = encrypt.encrypt(self.pubArgs['data'],self.deskey)
        data = { "sign"       :signature,
                 "version"    :self.version,
                 "deviceNo"   :self.deviceNo,
                 "deviceType" :self.deviceType,
                 "cityId"     :self.cityId,
                 "ticketId"   :'',
                 "fileStreams":'',
                 "openid"     :'', 
                 "data"       :strencrypt}
        self.res = self.client.post(self.host+self.port,data,catch_response=True)
        self.assertResult()
      
   
class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://test.passport.maifangma.com/"
    min_wait = 0
    max_wait = 0
    task_set = UserTasks