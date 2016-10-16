# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:59:53 2016

@author: shashank
"""
import sys
def dist(A,B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2

subtask = input()
T = input()
for i in range(T):
    A = []
    B = []
    C = []
    dis = []
    temp = sys.stdin.readline().split()
    A.append(float(temp[0]))
    A.append(float(temp[1]))
    B.append(float(temp[2]))
    B.append(float(temp[3]))
    C.append(float(temp[4]))
    C.append(float(temp[5]))
    dis = [dist(A,B),dist(B,C),dist(C,A)]
    ma = max(dis)
    dis.remove(ma)
    if subtask == 1:
        if (abs(dis[0] - dis[1])>10**-12 and abs(dis[0] - ma)>10**-12 and abs(dis[1] - ma)>10**-12):
            print 'Scalene triangle'
        else:
            print 'Isosceles triangle'
    if subtask == 2:
        if (ma == dis[0] + dis[1]) or (dis[0] == ma + dis[1]) or (dis[1] == dis[0] + ma):
            if (abs(dis[0] - dis[1])>10**-12 and abs(dis[0] - ma)>10**-12 and abs(dis[1] - ma)>10**-12):
                print 'Scalene right triangle'
            else:
                print 'Isosceles right triangle'
        elif (ma > dis[0] + dis[1]) or (dis[0] > ma + dis[1]) or (dis[1] > dis[0] + ma): 
            if (abs(dis[0] - dis[1])>10**-12 and abs(dis[0] - ma)>10**-12 and abs(dis[1] - ma)>10**-12):
                print 'Scalene obtuse triangle'
            else:
                print 'Isosceles obtuse triangle'
        else:
            if (abs(dis[0] - dis[1])>10**-12 and abs(dis[0] - ma)>10**-12 and abs(dis[1] - ma)>10**-12):
                print 'Scalene acute triangle'
            else:
                 print 'Isosceles acute triangle'
                
            
        
    
    
    
    