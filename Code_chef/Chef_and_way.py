# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:19:14 2015

@author: shashank
"""

#input_firstLine = (sys.stdin.readline()).split()
#N = int(input_firstLine[0])
#K = int(input_firstLine[1])
t = raw_input().split()
N = int(t[0])
K = int(t[1])
A = raw_input().split()
A = map(int,A)

product = 1 
def way(start,N,K,A):
    global product
    if N - start <= K:
        output = product*N
        print output        
        exit
    else:
        temp = min(A[1:K+1])
        product = product*temp
        way(A.index(temp)+1,N,K,A)


way(1,N,K,A)
        
    
        
    
    