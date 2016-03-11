x = 100
goods = [1,2,3,4,5,6,7,8,9]

def getNum(x, goods):
    if x <= 0 or len(goods) == 0:return 'params error'
    num = 0
    cost = 0
    goods.sort()
    while cost <= x and num < (len(goods)):
        cost += goods[num]
        if cost <= x :
            num += 1

    return num

print str(getNum(x, goods))
