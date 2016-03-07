def fibMetered(n):
    global numCalls
    numCalls += 1
    
    if n == 0 or n == 1:
        return 1
    else :
        return fibMetered(n - 1) + fibMetered(n - 2)

def testFib(n):
    global numCalls
    for i in range(n + 1):
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + 'times')
