import requests
import oss2  # oss2包 连接阿里云OSS的工具
import time
import os
from sys import argv
import urllib.parse
from shushan import post_file

auth = oss2.Auth('LTAIk26BvtLfOadg', 'FBBJdpWEFKIlve3VqjwdyEM9Ns4eAi')
endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'  # 地址
bucket = oss2.Bucket(auth, endpoint, 'shushan-static')  # 项目名称
# http://shushan-static.oss-cn-hangzhou.aliyuncs.com/mp3/UNIT2/
url = r'http://shushan-static.oss-cn-hangzhou.aliyuncs.com/'
# dir = r'./pinyin'
dir = argv[1]
my_open = open('./upload.txt', 'a', encoding="utf-8")

my_open.write('\n')
my_open.write('\n')
my_open.write(dir)
my_open.write('\n')


a = os.listdir(dir)
for file in a:
    file = dir + '/' + file
    result = post_file(file)
    my_open.write(result)
    my_open.write('\n')

my_open.close()