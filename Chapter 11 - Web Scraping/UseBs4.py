
import requests, bs4, html5lib

def Use_Bs4_WithHtml():
    res = requests.get('http://nostarch.com')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text)
    type(noStarchSoup)

def Use_Bs4_WithFile():
    exampleFile = open('example.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile, "html5lib")
    print(type(exampleSoup))

def Use_Select():
    exampleFile = open('example.html')          # 获取 File 对象
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html5lib")     # 获取 BeautifulSoup 对象

    # =================================================================
    # 测试 select(), 以抓取 id="author" 的元素为例
    # =================================================================
    print("--------------------- id=author 的元素 ------------------")
    elems = exampleSoup.select("#author")  # 调用 select(), 返回所有带 id="author" 的元素

    print(type(elems))            # 返回对象类型 : <class 'list'>
    print(len(elems))             # 返回 List对象长度为 : 1
    print(type(elems[0]))         # 返回List中元素的对象类型 : <class 'bs4.element.Tag'>
    print(elems[0])               # 返回整个标签内容 : <span id="author">Al Sweigart</span>
    print(elems[0].getText())     # 获取整个标签文本 : Al Sweigart
    print(elems[0].attrs)         # 获取元素内容(字典形式分成 key(标签名) - value(标签的文本))  {'id': 'author'}

    # =================================================================
    # 测试 select(), 找出所有<p>元素
    # =================================================================
    print("--------------------- 所有<p>标签的元素 ------------------")
    pElems = exampleSoup.select('p')

    i = 0
    while i < len(pElems):
        print(pElems[i])
        print(str(pElems[i]))       # 整个标签转换为文本
        print(pElems[0].getText())  # 取文本

        print()
        i = i + 1

# 使用 select() 返回的 Tag 对象
def Use_Tag():
    soup = bs4.BeautifulSoup(open('example.html'), "html5lib")
    spanElem = soup.select('span')[0]
    print(str(spanElem))
    print(spanElem.get('id'))
    print(spanElem.get('some_nonexistent_addr') == None)
    print(spanElem.attrs)


###########################################################
#
#              MAIN BODY OF SCRIPT
#
###########################################################
Use_Tag()




