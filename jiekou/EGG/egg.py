#coding=utf-8
'''
Created on 2016年7月25日

@author: quqiao
'''

from locust import HttpLocust, TaskSet, task


class UserTasks(TaskSet):
    def on_start(self):
        
        """ on_start is called when a Locust start before any task is scheduled """
        self.updatePassword()

    #@task
    #def login(self):
        #self.client.post("/login.do", {"mphone":"17713543052", "password":"123456"})

    #def logout(self):
        #self.client.post("/logout.do")
    
    @task   
    def updatePassword(self):
        self.client.post("/updatePassword.do", {"mphone":"17713543052", "password":"123456"})
        


            
        
class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """
    host = "http://192.168.1.153/egg-portal/authen"
    min_wait = 0
    max_wait = 0
    task_set = UserTasks




