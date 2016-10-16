# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:31:52 2015

@author: shashank
"""
input_file = open('A-large-practice.in')
output_file = open("output_storecredit_large222.txt", "w")
n = int(input_file.readline())
first = 0
second = 0
for k in range (n):
    
    c = int(input_file.readline())
    i = int(input_file.readline())
    t = input_file.readline().split()
    l=[]
    for p in t:
        l.append(int(p)) 
    for i in range (0,len(l)):
            for j in range (i+1,len(l)):
                if l[i]+l[j] == c:
                    first = min(i+1,j+1)
                    second = max(i+1,j+1)
    print >> output_file,'Case #%d: %d %d' %(k+1,first,second)
    