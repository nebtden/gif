import requests
import oss2  # oss2包 连接阿里云OSS的工具
import time
import os
import urllib.parse

auth = oss2.Auth('LTAIk26BvtLfOadg', 'FBBJdpWEFKIlve3VqjwdyEM9Ns4eAi')
endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'  # 地址
bucket = oss2.Bucket(auth, endpoint, 'shushan-static')  # 项目名称
# http://shushan-static.oss-cn-hangzhou.aliyuncs.com/mp3/UNIT2/
url = r'http://shushan-static.oss-cn-hangzhou.aliyuncs.com/'
dir = r'./pinyin'
my_open = open('./upload.txt', 'a', encoding="utf-8")

my_open.write('\n')
my_open.write(dir)
my_open.write('\n')


# 下边的方法是 我
def post_file(local_file):
    file = local_file[2:]
    # print(file)
    result = bucket.put_object_from_file(file, local_file)  # 括号内 左边是上传后的文件名，右边是当前系统的文件地址

    print('http status: {0}'.format(result.status))  # 打印上传的返回值 200成功
    # jpg_url = bucket.sign_url('GET', file)  # 阿里返回一个关于Zabbix_Graph.jpg的url地址 60是链接60秒有效

    # time.sleep(1)
    jpg_url = url+file
    # jpg_url = urllib.parse.unquote(jpg_url)
    # http: // shushan - static.oss - cn - hangzhou.aliyuncs.com / mp3 / UNIT1 / test.mp3
    my_open.write(jpg_url)
    my_open.write('\n')


#打开fie_name路径下的my_infor.txt文件,采用追加模式
#若文件不存在,创建，若存在，追加




# a = os.listdir(dir)
# for folder in a:
#     for file in os.listdir(dir + '/' + folder ):
#         file = dir + '/' + folder + '/' + file
#         post_mp3(file)
#
# my_open.close()
a = os.listdir(dir)
for file in a:
    file = dir + '/' + file
    post_file(file)
    # break

my_open.close()