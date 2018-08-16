import os
from upload import change_and_upload


my_open = open('./gif.txt', 'a', encoding="utf-8")
my_open.write('\n')
# 列出目录
for file in os.listdir('./original'):
    result = change_and_upload(file)
    my_open.write(result)
    my_open.write('\n')

my_open.close()