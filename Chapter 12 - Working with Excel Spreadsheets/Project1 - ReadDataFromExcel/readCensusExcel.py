#! python3

import openpyxl, pprint, os

print("Opening workbooking...")
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# TODO : 填充数据结构
# TODO: Fill in countyData with each county's population and tracts.
print("Reading rows...")
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state  = sheet['B' + str(row)].value # 拼单元格坐标字符串 ： 'B' + str(row) 即 B1, B2, ...
    county = sheet['C' + str(row)].value
    pop    = sheet['D' + str(row)].value

    # ------------------------------------------------------------------
    # 设置默认值。 不设的话后续取 key 进行登记 value 时报错。
    # Make sure the key for this state exists.
    # Make sure the key for this county in this state exists.
    #------------------------------------------------------------------
    countyData.setdefault(state, {})    # 如果键已经存在，setdefault()不会做任何事情
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # ------------------------------------------------------------------
    # 统计区数量 及 登记人口数量
    # Each row represents one census tract, so increment by one.
    # Increase the county pop by the pop in this census tract.
    # ------------------------------------------------------------------
    countyData[state][county]['tracts'] += 1      # 区数递增
    countyData[state][county]['pop'] += int(pop)  # 人口累加


# TODO : 将结果写入文件
# TODO: Open a new text file and write the contents of countyData to it.
print('Writing results...')
os.chdir('D:\\')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

