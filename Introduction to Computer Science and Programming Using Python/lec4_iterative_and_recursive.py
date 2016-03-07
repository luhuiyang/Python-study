def factL(n):
    #iterative
    ans = 1
    while n > 1:
        ans = ans * n
        n -=1
    return ans

def factR(n):
    #recursive
    if n == 1:
        return n
    else:
        return n*factR(n-1)
