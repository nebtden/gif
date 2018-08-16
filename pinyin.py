import os
from urllib import  request
import time

text_file = r'./pinyin.txt'
lines = []
base_url = "https://resources.allsetlearning.com/pronwiki/resources/pinyin-audio/"
with open(text_file, 'r') as f:
    for file in f:
        url = base_url + file
        print(file)
        file = file.replace('\n','')
        print(file)
        print("downloading with " + file)
        LocalPath = os.path.join('D:\python\image\pinyin\\', file).encode('utf-8')
        # os.path.join将多个路径组合后返回
        print(url)
        url = url.encode('uft-8')
        print(url)
        request.urlretrieve(url, LocalPath)
        time.sleep(0.5)
        # 第一个参数url:需要下载的网络资源的URL地址
        # 第二个参数LocalPath:文件下载到本地后的路径
        # break



print("downloading with urllib")