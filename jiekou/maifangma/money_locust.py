#coding=utf-8
'''
Created on 2016年7月25日

@author: quqiao
'''

from locust import HttpLocust,TaskSet, task
import encrypt
import demjson


def createPostDataString(pubArgs,data):
    postDataString = ''
    dataStr = '{'
    index = 0
    for (k,v) in data.items():
        dataStr =  dataStr + '\"' + k + '\"'+':'+'\"' + v + '\"'
        if index < len(data)-1 :
            dataStr =  dataStr +','
        index   = index + 1
    dataStr =  dataStr + '}'
    pubArgs['data'] = dataStr
    
    index = 0
    for (k,v) in pubArgs.items():
        if v != '':
            postDataString = postDataString+k+'='+v
            if index < len(pubArgs) - 2 :
                postDataString = postDataString +'&'
        index = index + 1
    return postDataString

def decodeDataToObj(content,deskey):
    print content
    resObj = demjson.decode(content)
    data   = resObj.get('data')
    dencryptData = encrypt.dencrypt(data,deskey)
    dataObj = demjson.decode(dencryptData)
    return dataObj

def assertResult(res):
    resObj = demjson.decode(res.content)
    if res.status_code != 200:
        res.failure("status code error")
    elif resObj.get('code') != 0:
        res.failure("msg code error")
    else:
        res.success()

class UserTasks(TaskSet):
    # for HTTP request
    desKey   = ''
    ticketId = '' 
    token    = '72465872a0ff482784a8985615792f4f'        
    def on_start(self):
        encrypt.initSdk(self.token)
        self.desKey    = encrypt.getToken()
        self.ticketId  = self.login(user='admin',password='123456')
    
    def login(self,user,password):
        # public arguments
        version    = '1.0.0'
        deviceNo   = '72465872a0ff482784a8985615792f4f'
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
        
        data = {
            'account'    : user,
            'password'   : password,
            'type'       : '1'
        }
        
        # post data string 
        postStr   = createPostDataString(pubArgs = pubArgs,data = data)
        signature = encrypt.signature(postStr, self.desKey)
        strencrypt = encrypt.encrypt(pubArgs['data'],self.desKey)

        data = { "sign"       :signature,
                 "version"    :version,
                 "deviceNo"   :deviceNo,
                 "deviceType" :deviceType,
                 "cityId"     :cityId,
                 "ticketId"   :ticketId,
                 "fileStreams":fileStreams,
                 "openid"     :openid, 
                 "data"       :strencrypt}

        res = self.client.post("/login",data,catch_response=True)
        #assertResult(res)
        dataObj = decodeDataToObj(res.content,self.desKey)
        return dataObj.get('ticketId')

    #@task
    def money(self):
        # public arguments
        version    = '1.0.0'
        deviceNo   = '72465872a0ff482784a8985615792f4f'
        deviceType = '2'
        cityId     = '51010000'
        ticketId   = self.ticketId
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
        
        data = {}
        
        # post data string 
        postStr   = createPostDataString(pubArgs = pubArgs,data = data)
        signature = encrypt.signature(postStr, self.desKey)
        strencrypt = encrypt.encrypt(pubArgs['data'],self.desKey)

        data = { "sign"       : signature,
                 "version"    : version,
                 "deviceNo"   : deviceNo,
                 "deviceType" : deviceType,
                 "cityId"     : cityId,
                 "ticketId"   : ticketId,
                 "fileStreams": fileStreams,
                 "openid"     : openid, 
                 "data"       : strencrypt}

        res = self.client.post("/user/modifymoney",data,catch_response=True)
        dataObj = decodeDataToObj(res.content,self.desKey)
        

   
class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://test.passport.maifangma.com/"
    min_wait = 0
    max_wait = 0
    task_set = UserTasks