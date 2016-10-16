# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:19:39 2015

@author: shashank
"""
import sys
T = sys.stdin.readline()
N_l = []
M_l = []
for j in range (T):
    n,m = sys.stdin.readline().strip()
    n = int(n)
    m = int(m)
    N_l.append (n)
    M_l.append (m)
for j in range (T):
    robots = []
    N = N_l[j]
    M = M_l[j]
    for i in range (M,N):
        robots.append([i+1,0])
    for i in range (M):
        robots.append([i+1,0])
    #print robots
    k = 0
    while True:
        if robots[k][1] == 0:
            robots[k][1] = 1
            k = robots[k][0] - 1
        else:
            break
    count = 0
    for i in range (N):
        if robots [i][1] == 0:
            count+=1
    if count == 0:
        print 'Yes'
    else:
        print 'No %d' %count
        
        
        
        