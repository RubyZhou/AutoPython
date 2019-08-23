#----------------------------------------------------------
# Title   : Files.py
# version : v1.0
# Create  : 2019/08/12 zhouyf
#
# Descripthion
#   读写文件
#
# Changes
#
#----------------------------------------------------------

###########################################################
# list of functions.
###########################################################
#
# funciton name            function purpose
# -----------------------  -----------------------------
# Usage()                  脚本的使用方法
#
###########################################################
# start of functions.
###########################################################

#
# Funtion : showdir()
#   显示目录下所有文件名
#
def showdir():
    path = 'C:\\Windows\\System32'
    #path = 'C:\\Windows\\System32\\calc.exe'

    print(os.path.basename(path))
    print(os.listdir('C:\\Friday & Saturday'))

#
# Funtion : txtRead()
#   读取文件, 输出到屏幕
#
def txtRead(myFile):
    txtFile = open(myFile)
    Content = txtFile.read()
    print(Content)
    txtFile.close()

#
# Funtion : txtWrite
#   写文件, 将目录下的所有文件名写到文件中
#
def txtWrite():
    txtFile = open('D:\\test\\hello.txt', 'w')
    for filename in os.listdir('C:\\Friday & Saturday'):
        txtFile.write(filename + '\n')
    txtFile.close()

#
# Funtion : shelveModel
#   通过 shelve模块保存变量
#
def shelveModel():
    print("# 开始写入shelve文件...")
    shelfFile = shelve.open('D:\\test\\hello1.txt')
    shelfFile['x'] = os.listdir('C:\\Friday & Saturday')
    shelfFile['y'] = os.listdir('C:\\Friday & Saturday')
    shelfFile.close()
    print("完毕.\n")

    print("# 获取shelve文件类型:")
    print(type(shelfFile))
    print()

    print("# 开始读取入shelve文件...")
    shelfFile = shelve.open('D:\\test\\hello1.txt')
    print(shelfFile['x'])
    shelfFile.close()
    print()

    print("# keys() & values()")
    shelfFile = shelve.open('D:\\test\\hello1.txt')
    print(list(shelfFile.keys()))
    print(list(shelfFile.values()))

#
# Funtion : ShowFolderTree
#   遍历目录树
#
def ShowFolderTree():
    # 遍历目录树
    for folderName, subforders, filenames in os.walk('C:\\Users\\zhouyf\\Desktop\\Library\\05 - 算法 & 设计模式'):
        print('\nThe current folder is ' + folderName)
        # 当前目录中的目录. 不递归, 仅一层; 仅子目录名, 不带完整路径
        for subforder in  subforders:
            print('    | SUBFORDER OF ' + folderName + ' : ' + subforder)

        # 当前目录中的文件
        for filename in filenames:
            print("    | FILE INSIDE " + folderName + " : " + filename)

#
# Funtion : UseZipFile
#   文件读取/解压/压缩
#
def UseZipFile():
    import zipfile
    os.chdir("D:\\test")

    # 读取压缩文件
    exampleZip = zipfile.ZipFile("test.zip")
    print(exampleZip.namelist())

    spamInfo = exampleZip.getinfo('hello.txt')
    print("压缩前大小 : ", spamInfo.file_size)
    print("压缩后大小 : ", spamInfo.compress_size)
    print("压缩率 : ", (round(spamInfo.compress_size/spamInfo.file_size*100, 2)) , "%")

    # 解压
    os.makedirs("D:\\test\\compress")
    exampleZip.extractall(path="D:\\test\\compress")
    exampleZip.close()

    #压缩文件
    newZip = zipfile.ZipFile("new.zip", 'w')
    newZip.write("hello.txt", compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()

###########################################################
# end of functions.
###########################################################


###########################################################
#
#              MAIN BODY OF SCRIPT
#
###########################################################
import os
import shelve

#shelveModel()
UseZipFile()

#myFile="D:\\test\\hello.txt"
#txtWrite()
#txtRead(myFile)
#txtWrite()













