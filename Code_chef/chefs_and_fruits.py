# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 22:53:04 2016

@author: shashank
"""
import sys
T = int(sys.stdin.readline())
output = []
for i in range (T):
    t = (sys.stdin.readline()).split()
    apple = int(t[0])
    orange = int(t[1])
    money = int(t[2])
    if apple < orange:
        if orange - apple <= money:
            output.append(0)
        else:
            output.append(orange - (apple + money))
    elif orange < apple:
        if apple - orange <= money:
            output.append(0)
        else:
            output.append(apple - (orange + money))
    else:
        output.append(0)
for i in range (T):
    print output[i]