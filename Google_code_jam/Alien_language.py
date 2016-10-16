# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:51:49 2015

@author: shashank
"""

words = ['abc','bca','dac','dbc','cba']
stri = '(ab)(bc)(ca)'
y =stri.replace('(',' ').replace(')',' ')
lst = y.split()
print lst
match = []
"""for i in range(len(lst[j])-1):
    for word in words:
        if word[i] == lst [0][i]:
            match.append(word)
print match"""