#! python3

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print("返回对象")
print(type(res))

print("请求结果:")
print(res.status_code)

print("返回文本长度")
print(len(res.text))

print("显示前 250 个字符")
print(res.text[:250])

print("------------------------------------------------")

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))