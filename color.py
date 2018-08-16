import numpy as np
from PIL import Image

# Convert Image to array
img = Image.open("out/8.png").convert('RGB')
arr = np.array(img)
size = arr.shape


for i in range(200,217):
    for j in range(70,130):
        r, g, b = arr[i, j]
        print(arr[i, j])
        # print(arr[i,j])

for i in range(size[0]):
    for j in range(size[1]):
        r,g,b = arr[i,j]
        if r==g==b :
            continue
        else:
            print(arr[i,j])
            # print('index',i,j)
            arr[i, j] = [0,0,0]
        # if r == 82 and g == 0 and b == 0:
        #     arr[i, j] = [3, 3, 3]
        # if r == 107 and g == 16 :
        #     arr[i, j] = [3, 3, 3]
        # if r == 99 and g == 16 :
        #     arr[i, j] = [3, 3, 3]
        # if r == 115 and g == 41 :
        #     arr[i, j] = [3, 3, 3]
        # if r == 123  and g == 49 and b == 49:
        #     arr[i, j] = [3, 3, 3]
        # if r == 140  and g == 74 and b == 74:
        #     arr[i, j] = [4, 4, 4]
        # if r>=60 and r<=150:
        #     arr[i, j] = [4, 4, 4]
        # elif r==g==b:
        #     continue
        # elif r==247 and g==247 and b==239 :
        #     continue
        # else:
        #     # print(i,j)
        #     # print(arr[i,j])
        #     pass
# img.show()




# Convert array to Image
img = Image.fromarray(arr)
# img.show()
img.save("out/frame88.png")
# print(arr.shape)
# print(arr[0][0])
# print(img.mode)
# print(arr)