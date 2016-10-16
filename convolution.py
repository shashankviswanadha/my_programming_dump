# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:40:05 2015

@author: shashank
"""

x=[8,3,1,2]
h=[2,7,1,3,1]
c=input('Enter a number')
summ=0
if (c>len(x)):
    print 0
else:
    for i in range (0,len(x)):
        summ=summ+x[i]*x[i-c]
        c-=2
   print summ