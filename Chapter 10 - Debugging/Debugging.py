#----------------------------------------------------------
# Title   : Debugging.py
# version : v1.0
# Create  : 2019/08/23 zhouyf
#
# Descripthion
#   程序调试
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
# Funtion : Usage()
#    脚本的使用方法
#
def Usage() :
    print("Usage")

#
# Funtion :
#    案例 1 ： raise 抛出异常
#
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
        print(symbol * width)


def test_Assert() :
    podBayDoorStatus = 'open'
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
    podBayDoorStatus = "I\'m sorry, Dave. I\'m afraid I can't dothat."
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

def test_logging():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.debug('Some debugging details.')
    logging.info('The logging module is working.')
    logging.warning('An error message is about to be logged.')
    logging.error('An error has occurred.')
    logging.critical('The program is unable to recover!')
    


#
# Funtion : 菜单
#
def DebuggingMenu():
    print("请输入功能编号：")
    answer=input()
    if answer == "1" :
        print("[eg.1] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
            try:
                boxPrint(sym, w, h)
            except Exception as err:
                print('An exception happened: ' + str(err))
    elif answer == "2" :
        print("[eg.2] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        test_Assert()
    elif answer == "3" :
        #print("[eg.3] >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        test_logging()
    else:
        print("输入有误。")



###########################################################
# end of functions.
###########################################################



###########################################################
#
#              MAIN BODY OF SCRIPT
#
###########################################################
import logging

DebuggingMenu()