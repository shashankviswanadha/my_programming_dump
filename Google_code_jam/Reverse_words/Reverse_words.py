# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:30:55 2015

@author: shashank
"""
input_file = open('B-small-practice.in')
output_file = open("output_reversewords_small.txt", "w")
n = int(input_file.readline())
for count in range(n):
    space_index = []
    reverse_line = None
    line = input_file.readline()
    for i in range (len(line)):
        if line[i] == ' ':
            space_index.append(i)
    #print space_index
    length_space = len(space_index)-1
    #print length_space
    for k in range(length_space,-1,-1):
        if k == length_space:
            reverse_line = line[space_index[k]+1:len(line)-1] + ' '
        else:
            reverse_line = reverse_line + line[space_index[k]+1:space_index[k+1]+1]
    if length_space == -1:
        reverse_line = line[:len(line)-1]
    else:
        reverse_line = reverse_line + line[:space_index[0]]
    #print reverse_line
    print >> output_file,'Case #%d: %s' %(count+1,reverse_line)