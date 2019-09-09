#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # 命令行读取
    address = ' '.join(sys.argv[1:])
else:
    # 剪切板读取
    address = pyperclip.paste()

# 龙之梦雅仕大厦
webbrowser.open('https://www.google.cn/maps/place/' + address)