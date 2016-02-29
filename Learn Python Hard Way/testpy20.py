file = open("test2.txt")
print file.readline()
print file.readline()
print file.readline()
file.seek(3)

print file.readline()
print file.readline()
print file.readline()