# -*- codeing = utf-8 -*-
# @Time :2022/4/7 13:59
# @Author:刘伟怡
# @File :testUrllib.py
# @Software :pyCharm

import urllib.request
import urllib.parse

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# data=bytes(urllib.parse.urlencode({"hello":"word"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

# try:
#
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
# except urllib.error.URLError as e:
#     print("time out")

url = "https://douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29 "
}
data=bytes(urllib.parse.urlencode({'name':'aaa'}),encoding='utf-8')
req = urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode('utf-8'))