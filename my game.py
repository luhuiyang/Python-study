# --coding: utf-8 --
from random import randint
number = 0
min_number = 0
max_number = 100

result = False

def check_number(x):
    global number
    global min_number
    global max_number
    if x==number:
        win()
    elif (x < max_number) and (x > number):
        max_number = x
        print_range()
    elif (x > min_number) and (x < number):
        min_number = x
        print_range()
    else:
        check_range()
        
def win():
    global result
    result = True
    print '恭喜你猜对了！'
        
def print_range():
    print '目前答案的范围是%d到%d（不包括%d和%d）' % (min_number, max_number, min_number, max_number)
    
def check_range():
    print '请重新输入答案范围内的数字'
    
def input_number():
    guess_number = int(raw_input('输入你猜的数字 >>'))
    check_number(guess_number)
    
def start_game():
    global number
    print '猜数字游戏'
    print '----------'
    number = randint(1, 99)
    print '随机数字已生成，游戏开始'
    print_range()
    while not result:
        input_number()

start_game()
