# -- coding: utf-8 --
#那年，你16岁，她也16岁。。。正是羞涩的年纪，为了更好地上课传纸条，她发明了一种新的加密方法防止其他同学的偷看。可是，你能解出她的这段密码吗？

#你拿到她传给你的纸条后，发现上面竟然是一堆乱码"h?lunc"这是什么意思呢？
#此时，你看到了另一串数字[1,2,3,4,5,0]和一个单独的数字2！
#你突发奇想，原来！你需要重组那句乱码，而每个字符对应的位置都是那串数字决定的。
#这样会不会太简单被破解了？所以，加上那个2意味着你要重组两次。
#
#
#我们看看该怎么做呢，首先"h?lunc"六个字符对应012345，按照123450的变换后成了"?lunch"，
#因为有个2，我们要变两次，"?lunch"对应012345,按照123450的顺序重组就成了"lunch?" 
#WOW原来是这个样子！
#写一段完整的代码（不仅仅是一个程序），给一个乱码字符串，一个数组，和一个整数，把破解好的密码print出来吧！
#
#例子:
#
#输入："ABC" [2,0,1] 2            输出："BCA"
#输入："ABCD" [3,2,1,0] 1         输出："DCBA"
#输入："12345" [3,1,2,4,0] 1      输出："42351"
#
#应该是abcd对应0123， 然后按照3210排序，若后面的数字为2，则解密2次
#此代码中，错误的理解为，将abcd对应3210，然后按0123排序，为dcba，然后输出1230，即cbad
def getCiphertext(str1, arrs, status):
    length = 0
    length = int(len(str1))
    if len(str1)!= len(arrs):
        return "error"
    else:
        if status == 0:
            print str1
            return str1
        str2 = []
        for i in range(length):
            str2.append('')
        for i in range(length):
            str2[arrs[i]] = str1[i]
            print 'i = ' + str(i)
            print 'str1['+str(i) +'] = ' + str1[i]
            print 'str2['+str(i) +'] = ' + str(str2)
        str1 = ''
        for i in str2:
            str1 += i
        print 'ans = ' + str1[1:] + str1[0]
        return getCiphertext(str1[1:] + str1[0], arrs, status-1)
        
arrs = [3, 2, 1, 0]
str1 = 'ABCD'
status = 1
print 'the anser is: ' + getCiphertext(str1, arrs, status)
