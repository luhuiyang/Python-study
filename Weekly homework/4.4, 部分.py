# -*- coding: utf-8 -*-
def getCount(a):
    b = a[::-1]
    total = 0
    for i in a:
        total = total + i
    print 'total = %d' % total
    if total == 0:
        print '最长数为 + %' % len(total)
    temp = total
    for j in range(len(a)):
        total = temp
        for x in range(len(b)):
            print 'i = %d , j = %d' % (j, x)
            if temp == 0:
                print 'lenth is %d ' % (len(a) - x - j)
                return len(a) - x - j-1
            else:
                total = total - b[x]
                print '总数是%d' % total
        temp = temp - a[j]
    print '错误'
    return 'error'
            
a = [0,1,2,3] 

getCount(a)