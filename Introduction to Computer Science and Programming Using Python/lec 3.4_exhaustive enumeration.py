x = float(raw_input('Enter a number: '))
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0

while (abs(ans**2-x)>epsilon) and (ans<x):
    ans += step
    numGuesses += 1

print ('NumGuesses = ' + str(numGuesses))
if ans >= x:
    print 'Failed on square root of ' + str(x)
else:
    print (str(ans) + 'is close to the square root of ' + str(x))
