
import openpyxl

nianji = '3down'
path = r'./mp3/rj_'+nianji+'/'
file_path = path+nianji+'.xlsx'
text_file = path+'text.txt'
wb = openpyxl.load_workbook(file_path)
sheet = wb.get_sheet_by_name('Sheet1')

print(file_path)
lines = []
with open(text_file, 'rt') as f:
    for line in f:
        # process line
        lines.append(line)




# unit = ''
print(sheet['A1'], sheet['A1'].value)
print(sheet['A2'], sheet['A2'].value)
print(sheet['B1'], sheet['B1'].value)
print(sheet['B2'], sheet['B2'].value)
print(sheet['C1'], sheet['C1'].value)
for row in sheet.rows:
    # row[6].value = 'sssssss'
    unit_value = row[1].value
    if not unit_value:
        continue
    unit_value = str.upper(row[1].value)
    unit_value = unit_value.replace(' ', '')

    title = row[2].value
    title = title.strip('?.!')
    title = title.lower()
    if unit_value == 'RECYCLE2' or unit_value =='RECYCLE1':
        # unit_value='RECYCLE2'
        pass
    myurl = 'http://shushan-static.oss-cn-hangzhou.aliyuncs.com'+path[1:]+unit_value+'/'+title

    print('myurl----')
    print('\n')
    print(myurl)
    print('\n')

    for line in lines:

        line = line.strip('?.!')
        line = line.lower()
        if myurl in line:

            row[6].value=line
    # 考虑到标点符号等因素，两边都去掉符号
    # if unit_value=='UNIT1':
    #     break

wb.save(file_path)