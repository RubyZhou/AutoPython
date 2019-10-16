#! python3

import requests, sys, webbrowser, bs4

print("binging....")
print(sys.argv[1:])


res = requests.get('https://cn.bing.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 调试
#webbrowser.open('https://cn.bing.com/search?q=' + ''.join(sys.argv[1:]))

# TODO: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html5lib")

# TODO: Open a browser tab for each result.
# 分析 html, 找 h2 标签下的 a 标签
linkElems = soup.select(('h2 > a'))

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print(linkElems[i])
    print(linkElems[i].getText)
    print(linkElems[i].get_text)
    print("---------")
    #webbrowser.open(linkElems[i].get('href'))
