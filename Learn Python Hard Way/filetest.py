file = open('sample.txt', 'w')

file.write('wwwww')

file.close()

current_file = open('sample.txt').read()

print current_file
