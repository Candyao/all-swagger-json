#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
import hug
import os
import json
executor = ThreadPoolExecutor(2)
def send_msg():
    file = {}
    file['all_url'] = []
    for var in os.listdir("/opt/swagger/dist/json"):
        one_url={}
        one_url['url']=var
        one_url['name']=var
        file['all_url'].append(one_url)
    return file


@hug.get()
def Pjson(body):
    try:
        p=executor.submit(send_msg)
        return p.result()
    except Exception as e:
        print(e)
        return {'code': -1, 'status': 'failed', 'message': '参数不正确！'}

if __name__ == '__main__':
    hug.API(__name__).http.serve(port=8890)  #python api 端口
