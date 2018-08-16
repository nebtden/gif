from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH

path_to_mp3 = r"./mp3/rj_3up/UNIT1/Hello, I'm Chen Jie.What's your name.mp3"
from mutagen.mp3 import MP3



import openpyxl

nianji = 'rj_3up'
path = r'./excel/'
file_path = path+nianji+'.xlsx'

wb = openpyxl.load_workbook(file_path)
sheet = wb.get_sheet_by_name('Sheet1')



for row in sheet.rows:
    if row[6].value=='链接':
        continue
    voice_url = row[6].value
    # http: // shushan - static.oss - cn - hangzhou.aliyuncs.com / mp3 / rj_3down / RECYCLE1 / He
    # 's my friend,John.mp3
    # print(voice_url)
    mp3_path = voice_url.replace('http://shushan-static.oss-cn-hangzhou.aliyuncs.com/','./')
    mp3_path = mp3_path.replace('\n','')
    audio = MP3(mp3_path)
    length = audio.info.length
    row[7].value = int(float(length)*1000)




wb.save(file_path)