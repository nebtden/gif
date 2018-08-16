from PIL import Image, ImageSequence
import numpy as np
import os, sys
argv = sys.argv
import time
from shushan import post_file,changecolor

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