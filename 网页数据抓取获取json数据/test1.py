#coding:utf-8

import urllib
import requests
import json
import types

#https://movie.douban.com/typerank?type_name=动作&type=5&interval_id=100:90&action=

post_param = {'action':'','start':'0','limit':'20'}
#headers = {'Content-Type': 'application/json'}
data = json.dumps(post_param)
return_data = requests.get("https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90",data, verify = False)

print (return_data.text)