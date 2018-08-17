import oss2  # oss2包 连接阿里云OSS的工具
from PIL import Image, ImageSequence
import numpy as np
import os, sys
argv = sys.argv
import time

def change_and_upload(filename):
    basename = os.path.basename(filename)
    filename = 'original/' + basename
    new_filename = 'gif/' + basename
    im = Image.open(filename)
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(im)


    # 列出目录
    for file in os.listdir('./out'):
        os.remove('./out/'+file)

    time.sleep(1)

    imgs = []
    index = 1
    # 遍历图片流的每一帧
    for frame in iter:

        img = frame.convert('RGB')
        frame.save("./out/%d.png" % index)
        # arr = np.array(frame)
        index += 1

    a = os.listdir('./out')
    # a.sort(key=lambda x : int(x[:-4]))
    a.sort(key=lambda x:int(x[:-4]))
    # a = sorted(a, key=lambda x: int(x[:-4]), reverse=True)
    print(a)
    for file in a:
        file = './out/'+file
        #
        img = Image.open(file).convert('RGB')
        arr = np.array(img)
        arr = changecolor(arr)
        frame = Image.fromarray(arr)
        frame.save(file)
        imgs.append(frame)


    # 把图片流重新成成GIF动图
    imgs[0].save(new_filename, save_all=True, append_images=imgs[1:])
    # time.sleep(0.5)
    result = post_file(new_filename)
    return result

auth = oss2.Auth('LTAIk26BvtLfOadg', 'FBBJdpWEFKIlve3VqjwdyEM9Ns4eAi')
endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'  # 地址
bucket = oss2.Bucket(auth, endpoint, 'shushan-static')  # 项目名称
# http://shushan-static.oss-cn-hangzhou.aliyuncs.com/mp3/UNIT2/
url = r'http://shushan-static.oss-cn-hangzhou.aliyuncs.com/'




def post_file(local_file):

    # 检测文件名是否为相对路径，如果是，则去掉./这样的符号
    if local_file.find('./')!=-1:
        file = local_file[2:]
    else:
        file = local_file
    # print(file)
    result = bucket.put_object_from_file(file, local_file)  # 括号内 左边是上传后的文件名，右边是当前系统的文件地址

    print('http status: {0}'.format(result.status))  # 打印上传的返回值 200成功
    # jpg_url = bucket.sign_url('GET', file)  # 阿里返回一个关于Zabbix_Graph.jpg的url地址 60是链接60秒有效

    # time.sleep(1)
    jpg_url = url+file
    # jpg_url = urllib.parse.unquote(jpg_url)
    # http: // shushan - static.oss - cn - hangzhou.aliyuncs.com / mp3 / UNIT1 / test.mp3
    return jpg_url


# 清空之前生成的图片
def changecolor(arr):
    size = arr.shape
    #直接根据大小更改
    if size[0] == 480:
        for i in range(size[0]):
            for j in range(size[1]):
                r, g, b = arr[i, j]
                if r == g == b:
                    continue
                else:
                    arr[i, j] = [0, 0, 0]
    else:
        for i in range(size[0]):
            for j in range(size[1]):
                r, g, b = arr[i, j]
                if r == g == b:
                    continue
                elif r >= 60 and r <= 150:
                    arr[i, j] = [4, 4, 4]

                elif r == 247 and g == 247 and b == 239:
                    continue
                else:
                    pass
    # img = Image.fromarray(arr)
    # # img.show()
    # img.save(file)
    return arr
