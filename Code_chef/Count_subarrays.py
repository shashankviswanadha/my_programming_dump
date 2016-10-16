# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:51:06 2015

@author: shashank
"""

import sys
T = int(sys.stdin.readline())
output = []
for i in range (T):
    N = int(sys.stdin.readline())
    B = sys.stdin.readline()
    A = map(int, B.split(" "))
    if len(A) == len(set(A)):
        if N == 1:
            output.append (1)
        else:
            output.append(N*(N-1)/2)
    if len(A) > len(set(A)):
        new_len = len(set(A))
        output.append((new_len*(new_len-1)/2) + len(A) - len(set(A)))
for ans in output:
    print ans
        