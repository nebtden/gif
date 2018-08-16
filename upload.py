import json
import base64
import os
import oss2



# 路径依赖
# 'KEY_ID'             => 'LTAIk26BvtLfOadg', // 阿里云oss key_id
# 'KEY_SECRET'         => 'FBBJdpWEFKIlve3VqjwdyEM9Ns4eAi', // 阿里云oss key_secret
# 'END_POINT'          => 'oss-cn-hangzhou.aliyuncs.com', // 阿里云oss endpoint
# 'BUCKET'             => 'shushan-static'  // bucken 名称
#


# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAIk26BvtLfOadg', 'FBBJdpWEFKIlve3VqjwdyEM9Ns4eAi')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'shushan-static')


with open('./mp3/UNIT1/test.mp3', 'rb') as fileobj:
    # Seek方法用于指定从第1000个字节位置开始读写。上传时会从您指定的第1000个字节位置开始上传，直到文件结束。
    # 准备回调参数。
    fileobj.seek(0, os.SEEK_SET)
    # Tell方法用于返回当前位置。
    current = fileobj.tell()
    print(current)
    result = bucket.put_object('simon', fileobj)
    print(result.status)
    # print(result.size)
    # print(result.name)






