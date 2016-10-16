# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:22:15 2015

@author: shashank
"""

input_file = open('C-small-practice.in')
output_file = open("output_C_small1.txt", "w")
n = int(input_file.readline())
for count in range (n):
    length = int(input_file.readline())
    t_a = input_file.readline().split()
    t_b = input_file.readline().split()
    a = []
    b = []
    for p in t_a:
        a.append(int(p))
    for q in t_b:
        b.append(int(q))
    for i in range (length):
        c=0
        for j in range (length):
             c = c+a[j-i]*b[j]
        print c
        if i == 0:
            minimum = c
        else:
            if c < minimum:
                minimum = c
    print >> output_file,'Case #%d: %d' %(count+1,minimum)
        
         
