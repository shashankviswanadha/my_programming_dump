# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 14:55:05 2015

@author: shashank
"""
import math
import matplotlib.pyplot as plt
import numpy as np
#r = abs (math.sqrt (5))
n=1
a = -0.3
b = 0.4
count = 0
output_file = open("swaroop_xy.txt", "w")
while n==1:
    result_u = []
    result_v = []
    X = []
    Y = []
    X_1 = []
    Y_1 = []
    result_u1 = []
    result_v1 = []
    common_factor = 300
    r = math.sqrt ((1-a)**2+b**2)
    for t in np.linspace (0,2*math.pi,3000):
        x = a + r* np.cos(t)
        y = b + r*np.sin(t)
        X.append(x)
        Y.append(y)
        temp = (x*x)+(y*y)
        u = x*(temp+1)/(temp)
        v = y*(temp-1)/(temp)
        result_u.append(u)
        result_v.append(v)
    """for t_1 in np.linspace (0,2*math.pi,10):
        x_1 = a + r* np.cos(t)
        y_1 = b + r*np.sin(t)
        X_1.append(x)
        Y_1.append(y)
        temp_1 = (x*x)+(y*y)
        u_1 = x*(temp_1+1)/(temp_1)
        v_1 = y*(temp_1-1)/(temp_1)
        result_u1.append(u)
        result_v1.append(v)"""
    while count< 10:
        X_1.append(X[count*common_factor])
        Y_1.append(Y[count*common_factor])
        result_u1.append(result_u[count*common_factor])
        result_v1.append(result_v[count*common_factor])
        count += 1
        
    
    
    plt.figure()
    plt.scatter(X_1,Y_1)
    plt.plot(X,Y)
    plt.scatter(result_u1,result_v1)
    plt.plot(result_u,result_v)
    plt.grid()
    plt.axes().set_aspect('equal', 'datalim')
    plt.savefig('swaroop_xy.jpg')
    a -= 0.1
    b += 0.1
    n += 1
print >> output_file,'X-Y\n',np.round(X_1,2),'\n',np.round(Y_1,2),'\n\nU-V\n',np.round(result_u1,2),'\n',np.round(result_v1,2)
