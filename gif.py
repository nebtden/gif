from PIL import Image, ImageSequence
import numpy as np
from PIL import Image
import os

# 处理图片更改颜色的函数
def changecolor(arr):
    size = arr.shape
    for i in range(size[0]):
        for j in range(size[1]):
            r, g, b = arr[i, j]

            if r >= 60 and r <= 150:
                arr[i, j] = [4, 4, 4]

    return arr


file_name = "gif/礴.gif"

# 读取GIF
im = Image.open(file_name)
# GIF图片流的迭代器
iter = ImageSequence.Iterator(im)

index = 1

# 清空之前生成的图片

imgs = []
index = 1
# 遍历图片流的每一帧
for frame in iter:
    # index = str(index)
    img = frame.convert('RGB')
    frame.save("./out/%d.png" % index)
    # arr = np.array(frame)
    index += 1
# frame0 = frames[0]
# frame0.show()



# 把图片流重新成成GIF动图
# imgs[0].save('out.gif', save_all=True, append_images=imgs[1:])

