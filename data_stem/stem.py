# -*- coding: utf-8 -*-
from stemming.porter2 import stem
from sys import argv

if len(argv) != 2:
    print "Usage: <file-to-stem>"
    exit()

#print "# Stemming the file: ", argv[1]

f = open(argv[1])
for line in f:
    for token in line.split():
        print stem(token),
    print
