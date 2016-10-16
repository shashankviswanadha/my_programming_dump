# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 11:30:00 2016

@author: shashank
"""
import sys
N = input()
temp = sys.stdin.readline().split()
T = []
R = []
for item in temp:
    R.append(int(item))
for i in range (1,N+1):
    T.append(i)
    
output = (set(T)-set(T).intersection(set(R)))
for op in output:
    print op,
    
