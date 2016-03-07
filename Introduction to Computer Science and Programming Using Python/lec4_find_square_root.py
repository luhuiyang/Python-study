def findroot(x, power, epsilon):
    if x < 0 and power%2 == 0:
        return 'params error'
    #in case x is a negtive number or a decimal
    low = min(-1, x)
    high = max(1, x)
    ans = (low + high) / 2.0

    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
    return ans
    
