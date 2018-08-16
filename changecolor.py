
import numpy as np
from PIL import Image



def changecolor(file):
    img = Image.open(file).convert('RGB')
    arr = np.array(img)
    size = arr.shape
    for i in range(size[0]):
        for j in range(size[1]):
            r, g, b = arr[i, j]
            if r == 90 and g == 0 and b == 0:
                arr[i, j] = [0, 0, 0]
            if r >= 60 and r <= 150:
                arr[i, j] = [4, 4, 4]
            elif r == g == b:
                continue
            elif r == 247 and g == 247 and b == 239:
                continue
            else:
                pass
    img = Image.fromarray(arr)
    # img.show()
    img.save(file)
    return arr


