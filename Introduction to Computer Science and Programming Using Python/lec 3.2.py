x = int(raw_input('Enter a integer: '))
for ans in range(abs(x)+1):
    if ans ** 3 == x:
        break
if ans **3 != x:
    print (str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print ('Cube root of ' + str(x) + ' is ' + str(ans))
