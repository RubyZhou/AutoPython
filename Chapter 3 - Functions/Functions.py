import random


# 带参数函数定义
def hello(name):
    print('Hello ' + name)


# 返回值
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


print(getAnswer(random.randint(1, 9)))

# 设置函数参数结束符
print('Hello', end='')
print('World')

# 设置函数参数分隔符
print('cats', 'dogs', 'mice', sep='|')


# 局部作用域中定义全局变量
def spam():
    global eggs
    eggs = 'spam'


# 使用异常
def spam1(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam1(2))
print(spam1(0))