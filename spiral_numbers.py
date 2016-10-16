# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 09:45:43 2015

@author: shashank
"""

n=input ('Enter the order of the square matrix')
a=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=input ('Enter value')
nc=n/2
print a[n/2][n/2]
d=2
x=n/2
y=n/2
for i in range(nc):
    x+=1
    for j in range(d):
        print [x][y]
        y+=1
    x-=1
    y-=1
    for j in range(d):
        print a[x][y]
        x-=1
    x+=1
    y-=1
    for j in range(d):
        print a[x][y]
        y-=1
    x+=1
    y+=1
    for j in range(d):
        print a[x][y]
        x+=1
    x-=1
    d+=2
    