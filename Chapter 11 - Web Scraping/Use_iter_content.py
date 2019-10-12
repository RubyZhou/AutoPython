#!python3

import requests

# 1. 请求
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# 2. 检查错误
res.raise_for_status()

# 3. 打开文件, 下载数据,  关闭文件
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000): # 100000字节
    playFile.write(chunk)
playFile.close()
