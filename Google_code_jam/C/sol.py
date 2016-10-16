# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:11:37 2015

@author: shashank
"""

f = open('C-small-practice.in', 'r')

cases = int(f.readline())

for i in range (0, cases):
    nrOfIntegers = f.readline()
    xs = f.readline()
    ys = f.readline()

    x = [int(s) for s in xs.split()]
    y = [int(s) for s in ys.split()]

    x.sort()
    y.sort()
    sum = 0
    size = len(x)

    for j in range(0, size):
        sum+= int(x[j])* int(y[size -1 - j])

    print sum
