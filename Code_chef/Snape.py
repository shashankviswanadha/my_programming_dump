# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:54:00 2016

@author: shashank
"""
import sys
import math
T = input()
for i in range(T):
    BLS = sys.stdin.readline().split()
    print math.sqrt(float(BLS[1])**2 - float(BLS[0])**2),math.sqrt(float(BLS[0])**2 + float(BLS[1])**2)
    