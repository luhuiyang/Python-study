from sys import argv

script, filename = argv

print "erase file %r" % filename

#raw_input("???")

target = open(filename, "w")

print "overwrite"

#target.truncate()

line1 = raw_input("1:")
line2 = raw_input("2:")

print "lalala"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")

print "final,close"
target.truncate(5)

target.close()