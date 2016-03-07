x = float(raw_input('Enter a float between 0 and 1: '))

p = 0
while (x*(2**p))%1 != 0:
    print ('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p = p + 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2

for i in range(p - len(result)):
    result = '0' + result;

result = result[0:-p] + '0.' + result[-p:]
print('The binary representatition of the decimal ' + str(x) + ' is ' + str(result))
