from PIL import Image, ImageSequence
import numpy as np
# import changecolor
import os, sys
argv = sys.argv
import time
from shushan import post_file

basename = argv[1]
print(basename)

filename = 'original/'+basename+'.gif'
new_filename = 'gif/'+basename+'.gif'

im = Image.open(filename)
# GIF图片流的迭代器
iter = ImageSequence.Iterator(im)


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
    img = Image.fromarray(arr)
    # img.show()
    img.save(file)
    return arr

# 列出目录
for file in os.listdir('./out'):
    os.remove('./out/'+file)

time.sleep(3)

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
    imgs.append(frame)


# 把图片流重新成成GIF动图
imgs[0].save(new_filename, save_all=True, append_images=imgs[1:])
time.sleep(1)
result = post_file(new_filename)
print(result)