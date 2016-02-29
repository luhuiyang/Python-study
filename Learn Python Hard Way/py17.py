# --coding: utf-8 --
# from sys import argv
from os.path import exists

from_file = raw_input("from_file>>>")
to_file = raw_input("to_file>>>")
print "从文件 %s 拷贝到 %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "文件大小%d" % len(indata)

print "输出文件是否存在？%r" % exists(to_file)

output = open(to_file, "w")

output.write(indata)

print "ok"

output.close()

input.close()