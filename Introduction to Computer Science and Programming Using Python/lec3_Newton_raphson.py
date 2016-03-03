x = float(raw_input('Enter a number: '))
epsilon = 0.01
guesses = x/2

while (abs(guesses**2) - x)>=epsilon:
    guesses = guesses - (guesses**2 - x)/(2 * guesses)
    print str(guesses)

print ('Square root of ' + str(x) + ' is about ' + str(guesses))
