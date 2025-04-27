import requests
import json
import urllib3
import uuid
import os
# 忽略 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class ZoomEyePlugin:
    def __init__(self,username=None, password=None,ip=None,port=None,token=None):
        self.username=username
        self.password=password
        self.zoomeye_ip=ip
    def get_token(self):
        url=f"https://{self.zoomeye_ip}/api/v4/external/login"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': self.username,
            'password': self.password
        }
        try:
            response = requests.post(url, headers=headers, json=data,verify=False)
        except requests.exceptions.RequestException as e:
            return False
        if response.status_code != 200:
            return False
        return json.loads(response.text)['data']['token']
    
    def create_task(self,task_name,ip_str,port_str):
        url=f"https://{self.zoomeye_ip}/api/v4/external/detection"
        headers={
            'b-json-web-token':self.get_token()
        }
        target_list=ip_str.split(',')
        ports_list=port_str.split(',')
        data={
            'name':task_name,
            'target':target_list,
            'ports':ports_list,
            'protocol':["tcp"]
        }
        try:
            response=requests.post(url=url,headers=headers,json=data,verify=False)  # Changed 'data' to 'json'
        except requests.exceptions.RequestException as e:
            return False
        if response.status_code!=200:
            return response.text
        return response.json()['data']['taskId']
    
    def get_task_status(self,task_id):
        url=f"https://{self.zoomeye_ip}/api/v4/external/taskInfo?taskId={task_id}"
        headers={
            'b-json-web-token':self.get_token()
        }
        try:
            response=requests.get(url=url,headers=headers,verify=False)
        except requests.exceptions.RequestException as e:
            return False
        if response.status_code!=200:
            return response.text
        return response.json()['data']['status']
    
    def get_task_result(self,task_id):
        url=f"https://{self.zoomeye_ip}/api/v4/external/detection?taskId={task_id}"
        headers={
            'b-json-web-token':self.get_token()
        }
        response=requests.get(url=url,headers=headers,verify=False)
        count=response.json()['data']['count']
        page=response.json()['data']['page']
        page_size=response.json()['data']['pageSize']
        id=uuid.uuid4()
        tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        result_file = os.path.join(tmp_dir, f"result_{id}.txt")
        result_list=self.result(response)
        self.write_result(result_list,result_file)
        for page in range(2,int(count/page_size)+2):
            url=f"https://{self.zoomeye_ip}/api/v4/external/detection?taskId={task_id}&page={page}"
            try:
                response=requests.get(url=url,headers=headers,verify=False)
            except requests.exceptions.RequestException as e:
                return False
            result_list=self.result(response)
            self.write_result(result_list,result_file)
        return result_file
    
    def write_result(self,result_list,result_file):
        with open(result_file,'a') as f:
            for ip_port in result_list:
                f.write(json.dumps(ip_port) + '\n')

    def result(self,response):
        ip_port_list=[]
        for ip_port in response.json()['data']['list']:
            ip=ip_port['ip']
            for ports in ip_port['ports']:
                port=ports['port']
                service=ports['service']
                ip_port_list.append(
                    {
                        'host':ip,
                        'port':port,
                        'status':'opened',
                        'service':service
                    }
                )
        return ip_port_list
    def delete_task(self,task_id):
        url=f"https://{self.zoomeye_ip}/api/v4/external/deleteTask"
        headers={
            'b-json-web-token':self.get_token()
        }
        data={
            "taskId":task_id
        }
        try:
            response=requests.post(url=url,headers=headers,json=data,verify=False)
        except requests.exceptions.RequestException as e:
            return False
        if response.status_code!=200:
            return False
        return True
    
    def stop_task(self,task_id):
        url=f"https://{self.zoomeye_ip}/api/v4/external/stopTask"
        headers={
            'b-json-web-token':self.get_token()
        }
        data={
            "taskId":task_id
        }
        try:
            response=requests.post(url=url,headers=headers,json=data,verify=False)
        except requests.exceptions.RequestException as e:
            return False
        if response.status_code!=200:
            return False
        return True
    
    def get_status(self):
        url=f"https://{self.zoomeye_ip}/api/v4/external/login"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': self.username,
            'password': self.password
        }
        try:
            response = requests.post(url, headers=headers, json=data,verify=False)
        except requests.exceptions.RequestException as e:
            return False
        if response.status_code != 200:
            return False
        return True
