# --coding: utf-8 --
# from sys import argv
from os.path import exists

from_file = raw_input("from_file>>>")
to_file = raw_input("to_file>>>")
print "���ļ� %s ������ %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()

print "�ļ���С%d" % len(indata)

print "����ļ��Ƿ���ڣ�%r" % exists(to_file)

output = open(to_file, "w")

output.write(indata)

print "ok"

output.close()

input.close()