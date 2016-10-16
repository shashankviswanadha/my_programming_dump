# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:52:33 2015

@author: shashank
"""
import numpy as np
import matplotlib.pyplot as plt
X = 4
Y = 4
h = 0.04
M = 26#X/h + 1
N = 11#Y/h + 1
w = 1
phi = []
phi_old = []
max_error = 0
e = 0.01


for J in range (N):
    phi.append ([])
    
    for I in range (M):
        
        phi[J].append (0.0)
#print phi
#phi [2][1] = 1
#print phi
def left_function (i):
    y = (N-1-i)*h
    v = 4.0*y*(y-0.4)
    return v
    
def interior_point (i,j):
    phi [i][j] = (phi [i-1][j] + phi [i+1][j] + phi [i][j-1] + phi[i][j+1])/4.0
def left_semi_boundary (i,j):
   
    #print y,v
    phi [i][j] = (phi [i+1][j] + phi [i][j+1] + phi [i-1][j] - left_function(i)*h)/3.0
def top_semi_boundary (i,j):
    phi [i][j] = (phi [i][j+1] + phi [i+1][j] + phi[i][j-1])/3.0
def bottom_semi_boundary (i,j):
    phi [i][j] = (phi [i-1][j] + phi [i][j+1] + phi [i][j-1])/3.0
def right_semi_boundary (i,j):
    phi [i][j] = (phi [i][j-1] + phi [i+1][j] + phi [i-1][j])/4.0
    
    
    
    

while True:
#for k in range (10): 
    for J in range (N):
        phi_old.append ([])
    
        for I in range (M):
        
            phi_old[J].append (phi[J][I])
    #phi_old[I][J] = [[phi [I][J] for J in range(M)]for I in range(N)]
    #print phi_old
    #print phi
    for i in range (N-2,0,-1):
            
            for j in range (1,M-1):
                
                if ((i == 1) or (i == M-2) or (j == N-2) or (j == 1)):
                    if j == 1 and (i != 1 or i !=M-2):
                        
                        left_semi_boundary (i,j)
                    elif i == 1 and j != 1:
                        top_semi_boundary (i,j)
                    elif i == M-2 and (j != 1 and j != N-2):
                        bottom_semi_boundary (i,j)
                    elif j == N-2 and (i != 1 or i != M-2):
                        right_semi_boundary (i,j)
                    elif i == M-2 and j == 1:
                        phi [i][j] = (phi [i-1][j] + phi [i][j+1] - left_function(i)*h)/2.0
                    elif i == 1 and j == 1:
                        phi [i][j] = (phi [i+1][j] + phi [i][j+1] - left_function(i)*h)/2.0
                    elif i == M-2 and j == N-2:
                        phi [i][j] = (phi [i-1][j] + phi [i][j-1])/3.0
                    elif i == 1 and j == N-2:
                        phi [i][j] = (phi [i+1][j] + phi [i][j-1])/3.0
                else:
                    interior_point (i,j)
                phi [i][j] = w*phi [i][j] + (1-w)*phi_old [i][j]
                error = (phi[i][j] - phi_old [i][j])
    #print phi_old
                #print phi [i][j], phi_old [i][j]
                
                print "i=",i,"j=",j,"error=",error
                if max_error < abs(phi[i][j] - phi_old [i][j]):
                    max_error = abs(phi[i][j] - phi_old [i][j])
    if max_error < e:
        break
print phi

def vel_x(i,j):
    return (phi[i][j+1]+phi[i][j-1])/2.0
def vel_y(i,j):
    return (phi[i+1][j]+phi[i-1][j])/2.0
x=[i for i in range(1,M-1)]
y=[vel_x(5,i) for i in range(1,M-1)]
x1=[i for i in range(1,N-1)]
y1=[vel_y(i,20) for i in range(1,N-1)]

plt.plot(x,y)
