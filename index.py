from PIL import Image, ImageSequence
import numpy as np
# import changecolor
import os, sys


im = Image.open("images/lei.gif")
# GIF图片流的迭代器
iter = ImageSequence.Iterator(im)


# 清空之前生成的图片
def changecolor(arr):
    size = arr.shape
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
# print("目录为: %s" % os.listdir('./out'))
# for file in os.listdir('./out'):
#     os.remove('./out/'+file)

imgs = []
index = 1
# 遍历图片流的每一帧
for frame in iter:
    # print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
    # print(frame.mode)
    # frame.convert("RGB")

    img = frame.convert('RGB')
    frame.save("./out/%d.png" % index)
    # arr = np.array(frame)
    index += 1

a = os.listdir('./out')
a.sort()
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
imgs[0].save('out.gif', save_all=True, append_images=imgs[1:])