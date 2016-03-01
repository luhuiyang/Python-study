# --coding: utf-8 --
from sys import exit

def open_the_door():
    print '打开了门,前面有两个通道'
    print '你要前往哪个通道'
    lorr = raw_input('L or R>>')
    if 'L' in lorr or 'l' in lorr:
        turn_left()
        
    elif 'R' in lorr or 'r'  in lorr:
        turn_right()

    else:
        print '只能输入l或者r!'

def wait_for_death():
    print '那你就等死吧'
    exit(0)

def dead ():
    print '最后你死了'
    exit(0)

def fight_fail():
    print '你打不过它'
    dead()
    
def turn_left():
    print '左边有个出口，但是那里有头熊!'
    print '要不要打他'
    forn = raw_input('Y or N>>')
    if 'Y' in forn or 'y' in forn:
        fight_fail()
        
    if 'N' in forn or 'n' in forn:
        wait_for_death()

    else:
        print '只能输入y或者n!'

def turn_right():
    print '那里有个出口，但是门口有条大虫子!'
    print '要不要打他'
    forn = raw_input('Y or N>')
    if 'Y' in forn or 'y' in forn:
        fight_succeed()
        
    elif 'N' in forn or 'n' in forn:
        wait_for_death()

    else:
        print '只能输入y或者n!'

def fight_succeed():
    print '你打死了虫子!'
    survival()

def survival():
    print '你终于逃出来了'

print '一觉醒来，你发现你在一个昏暗的房间里，房间有一道关闭着的门，要不要打开他？'

next = raw_input('Y or N>>')

if 'Y' in next or 'y' in next:
    open_the_door()
elif 'N' in next or 'n' in next:
    wait_for_death()
else:
    print '只能输入y或者n!'
