# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:04:20 2016

@author: shashank
"""

N = input()
for i in range(N):
    n = 2
    T = input()
    summ = 0
    c = 1
    while n > 1:
        n = T/(5**c)
        summ = summ + int(round(n))
        c += 1
    print summ
        
        
        
        