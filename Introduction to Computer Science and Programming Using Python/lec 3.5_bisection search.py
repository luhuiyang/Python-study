# Besection search for square root

x = float(raw_input('Enter a number: '))
epsilon = 0.01
numGuesses = 0
ans = 0.0
low = 0.0
high = x
while (abs(ans**2-x)>epsilon):
    print 'low = ' + str(low) + ', high = ' + str(high) + ', ans = ' + str(ans)
    numGuesses += 1
    if ans**2<x:
        low = ans
    else:
        high = ans
    ans = (low+high)/2
print ('numGuesses = ' + str(numGuesses))
print str(ans) + 'is close to the square root of ' + str(x)
