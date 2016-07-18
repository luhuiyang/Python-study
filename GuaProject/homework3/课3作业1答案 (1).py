# 这里是两个字符串, 包含了大写字母和小写字母
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 字符串有一个 find 函数
# 可以返回 参数 在字符串中的首次出现的下标
# 例如
print(lower.find('e'))
# 4
print(lower.find('E'))
# -1 因为找不到


# 例子
# 返回字符串的小写形式
# 注意, 假设 s 字符串全是大写字母
def lowercase(s):
    # 初始化一个空字符串
    result = ''
    # 遍历字符串
    for c in s:
        # log('for c in s', c)
        # 对每一个字符串, 找到它在 upper 中的下标
        i = upper.find(c)
        # 然后把它加到 result 中
        # result = result + lower[i]
        # 下面的 += 相当于上面的语句, 是一个简便的写法
        result += lower[i]
    # 返回结果
    return result


# 1
# 定义一个函数
# 参数是一个字符串 s
# 返回大写后的字符串
# 注意, 假设 s 字符串全是小写字母
# def uppercase(s):
def uppercase(s):
    # 初始化一个空字符串
    result = ''
    # 遍历字符串
    for c in s:
        # 对每一个字符串, 找到它在 lower 中的下标
        i = lower.find(c)
        # 然后把它加到 result 中
        result += upper[i]
    # 返回结果
    return result



# 2
# 让 lowercase 能正确处理带 小写字母 的字符串
def lowercase(s):
    result = ''
    for c in s:
        i = upper.find(c)
        if i == -1:
            # 没找到, 说明不是大写字母, 不做处理
            result += c
        else:
            # 找到, 说明它是大写字母
            result += lower[i]
    return result


# 3
# 让 uppercase 能正确处理带 大写字母 的字符串
def uppercase(s):
    result = ''
    for c in s:
        i = lower.find(c)
        if i == -1:
            # 没找到, 说明不是小写字母, 不做处理
            result += c
        else:
            # 找到, 说明它是小写字母
            result += upper[i]
    return result


# 4
# 凯撒加密
# 对于一个字符串, 整体移位, 就是加密
# 假设移 1 位
# 原始信息 'afz' 会被加密为 'bga'
# 实现 encode, 把明文加密成密码并返回
# 移 1 位
# def encode(s)
def encode(s):
    result = ''
    for c in s:
        i = lower.find(c)
        new_index = (i + 1) % 26
        code = lower[new_index]
        result += code
    return result

# print(encode('afz'))


# 5
# 实现 decode, 把密码解密为明文并返回
# 移 1 位
# def decode(s)
def decode(s):
    result = ''
    for c in s:
        i = lower.find(c)
        # 下面这个运算是为了保证下标不为负数, 反正要对 26 取模(求余数)
        new_index = (i + 26 - 1) % 26
        code = lower[new_index]
        result += code
    return result

# print(decode('bga'))


# 6
# 实现新的 encode
# 多了一个参数 shift 表示移的位数
# def encode(s, shift)
def encode(s, shift):
    result = ''
    for c in s:
        i = lower.find(c)
        new_index = (i + shift) % 26
        code = lower[new_index]
        result += code
    return result


# 7
# 实现新的 decode
# 多了一个参数 shift 表示移的位数
# def decode(s, shift)
def decode(s, shift):
    result = ''
    for c in s:
        i = lower.find(c)
        # 下面这个运算是为了保证下标不为负数, 反正要对 26 取模(求余数)
        new_index = (i + 26 - shift) % 26
        code = lower[new_index]
        result += code
    return result


# 8
# 实现新的 encode
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号
# 则不做任何处理保留原样
# def encode(s, shift)
def encode(s, shift):
    result = ''
    for c in s:
        i = lower.find(c)
        # 没找到, 说明不做处理
        if i == -1:
            result += c
        else:
            new_index = (i + shift) % 26
            code = lower[new_index]
            result += code
    return result

# encode('a,b', 1)
# 'b,c'

# 9
# 实现新的 decode
# 多了一个参数 shift 表示移的位数
# 如果 s 中包含了不是字母的字符, 比如空格或者其他符号, 则不做任何处理保留原样
# def decode(s, shift)
def decode(s, shift):
    '''
    不要理会下面这几行注释, 上课会讲
    :type s: str
    :type shift: int
    :rtype: str
    :param s: 要解密的字符串
    :param shift: 移动的位数
    :return: 解密后的字符串
    '''
    result = ''
    for c in s:
        i = lower.find(c)
        if i == -1:
            result += c
        else:
            # 下面这个运算是为了保证下标不为负数, 反正要对 26 取模(求余数)
            new_index = (i + 26 - shift) % 26
            code = lower[new_index]
            result += code
    return result


# 10
# 知乎有一个求助题, 破译密码的
# 当然了, 根据普通人定律, 小孩子喜欢用这种方式表白...
# 链接在此
# https://www.zhihu.com/question/28324597
# 另, 这一看就是凯撒加密...
# 如果没思路, 可看本文件最后的提示
# 我把密码放在下面, 请解出原文
s = 'VRPHWLPHV L ZDQW WR FKDW ZLWK BRX,EXW L KDYH QR UHDVRQ WR FKDW ZLWK BRX'

# 不知道 shift 是多少, 所以 1 - 26 都试试
# 我们的程序只处理了小写, 所以先转成小写
s_lower = lowercase(s)
for shift in range(26):
    source = decode(s_lower, shift)
    print(source)

# 出来的结果是这 26 个, 人肉分析可得结果
# vrphwlphv l zdqw wr fkdw zlwk brx,exw l kdyh qr uhdvrq wr fkdw zlwk brx
# uqogvkogu k ycpv vq ejcv ykvj aqw,dwv k jcxg pq tgcuqp vq ejcv ykvj aqw
# tpnfujnft j xbou up dibu xjui zpv,cvu j ibwf op sfbtpo up dibu xjui zpv
# sometimes i want to chat with you,but i have no reason to chat with you
# rnldshldr h vzms sn bgzs vhsg xnt,ats h gzud mn qdzrnm sn bgzs vhsg xnt
# qmkcrgkcq g uylr rm afyr ugrf wms,zsr g fytc lm pcyqml rm afyr ugrf wms
# pljbqfjbp f txkq ql zexq tfqe vlr,yrq f exsb kl obxplk ql zexq tfqe vlr
# okiapeiao e swjp pk ydwp sepd ukq,xqp e dwra jk nawokj pk ydwp sepd ukq
# njhzodhzn d rvio oj xcvo rdoc tjp,wpo d cvqz ij mzvnji oj xcvo rdoc tjp
# migyncgym c quhn ni wbun qcnb sio,von c bupy hi lyumih ni wbun qcnb sio
# lhfxmbfxl b ptgm mh vatm pbma rhn,unm b atox gh kxtlhg mh vatm pbma rhn
# kgewlaewk a osfl lg uzsl oalz qgm,tml a zsnw fg jwskgf lg uzsl oalz qgm
# jfdvkzdvj z nrek kf tyrk nzky pfl,slk z yrmv ef ivrjfe kf tyrk nzky pfl
# iecujycui y mqdj je sxqj myjx oek,rkj y xqlu de huqied je sxqj myjx oek
# hdbtixbth x lpci id rwpi lxiw ndj,qji x wpkt cd gtphdc id rwpi lxiw ndj
# gcashwasg w kobh hc qvoh kwhv mci,pih w vojs bc fsogcb hc qvoh kwhv mci
# fbzrgvzrf v jnag gb pung jvgu lbh,ohg v unir ab ernfba gb pung jvgu lbh
# eayqfuyqe u imzf fa otmf iuft kag,ngf u tmhq za dqmeaz fa otmf iuft kag
# dzxpetxpd t hlye ez nsle htes jzf,mfe t slgp yz cpldzy ez nsle htes jzf
# cywodswoc s gkxd dy mrkd gsdr iye,led s rkfo xy bokcyx dy mrkd gsdr iye
# bxvncrvnb r fjwc cx lqjc frcq hxd,kdc r qjen wx anjbxw cx lqjc frcq hxd
# awumbquma q eivb bw kpib eqbp gwc,jcb q pidm vw zmiawv bw kpib eqbp gwc
# zvtlaptlz p dhua av joha dpao fvb,iba p ohcl uv ylhzvu av joha dpao fvb
# yuskzosky o cgtz zu ingz cozn eua,haz o ngbk tu xkgyut zu ingz cozn eua
# xtrjynrjx n bfsy yt hmfy bnym dtz,gzy n mfaj st wjfxts yt hmfy bnym dtz
# wsqixmqiw m aerx xs glex amxl csy,fyx m lezi rs viewsr xs glex amxl csy


# 请在做出这道题后, 观摩知乎链接中的各个答案, 好好地吸取大神们的营养

# 10 题提示
# 没有给出 shift 信息, 怎么办?
#
# 强行试出来

import 课4上课

