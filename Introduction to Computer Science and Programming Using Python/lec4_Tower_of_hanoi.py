# -- coding: utf-8 --
def printMove(fr, to):
    print('将第' + str(fr) + '根柱子上最上面一个原盘移动到第' + str(to) + '根柱子')

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
