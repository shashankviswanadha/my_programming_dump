# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:37:18 2016

@author: shashank
"""
import sys
def function (string):
    balance = 0
    max_balance = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == '(':
            balance += 1
        else:
            balance -= 1
        max_balance = max(max_balance,balance)
    return max_balance
    
T = int(sys.stdin.readline())
output = ['' for i in range(T)]
for i in range(T):
    A = sys.stdin.readline()
    FA = function(A)
    for j in range(FA):
        output[i] = output[i] + '('
    for j in range(FA):
        output[i] = output[i] + ')'

for item in output:
    print item
        
 
        
    