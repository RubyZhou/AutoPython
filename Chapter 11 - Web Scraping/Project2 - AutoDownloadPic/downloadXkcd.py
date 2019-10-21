#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = "https://xkcd.com"
dirPath = "C:\\Users\\zhouyf\\Desktop\\TEMP\\xkcd"
os.makedirs(dirPath, exist_ok=True)

while not url.endswith('#'):

    # Download the page. (下载网页)
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html5lib')

    # Find the URL of the comic image. (调用开发者工具进行分析, 下载图片)
    comicElem = soup.select('#comic img')

    if comicElem == []:     # Tips : '[]' 表示一个空对象
        print('Could not find comic image')
    else:
        # Download the image.
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)    # 再次调用 requests 加载图片网址
        res.raise_for_status()

    # Save the image to ./xkcd. (将图片保存至本地目录)
    imageFile = open(os.path.join(dirPath, os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url. （寻找下一个链接）
    prevLink = soup.select('a[rel=prev]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


print("done")

