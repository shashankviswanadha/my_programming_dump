# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:11:04 2016

@author: shashank
"""

import sys
T = int(sys.stdin.readline())
output = [[]for i in range(T)]
for i in range (T):
    phrase = []
    NandK = (sys.stdin.readline()).split()
    N = int(NandK[0])
    K = int(NandK[1])
    words = (sys.stdin.readline()).split()
    for j in range (K):
        temp_phrase = (sys.stdin.readline()).split()
        phrase = phrase + temp_phrase[1:]
    for k in range (N):
        if words[k] in phrase:
            output[i].append("YES")
        else:
            output[i].append("NO")

for i in range(T):
    length = len(output[i])
    for j in range (length):
        if j == length - 1:
            print output[i][j]
        else:
            print output[i][j],