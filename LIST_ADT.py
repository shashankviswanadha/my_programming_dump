# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:38:26 2016

@author: Shashank Viswanadha
"""

class array_list:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.elements = [None for i in range(self.maxsize)]
        self.last = 0

def end(L):
    if L.last == 0:
        return 0
    return L.last
    
def endElement(L):
    if L.last == 0:
        return 0
    return L.elements[L.last-1]
    
def first(L):
    if L.last == 0:
        return end(L)
    return L.elements[0]

def insert(x,p,L):
    if p == 0:
        L.elements[p] = x 
        L.last =+ 1
    elif p < L.last:
        t = L.elements[p]
        L.elements[p] = x
        for i in range(p+1,L.last):
            temp = L.elements[i]
            L.elements[i] = t
            t = temp
        L.elements[L.last] = t
        L.last += 1       
    elif p == L.last:
        L.elements[p] = x
        L.last += 1
    else:
        print "Cannot add",x
            
def locate(x,L):
    for i in range(L.last):
        if x == L.elements[i]:
            return i
    return end(L)

def retrieve(p,L):
    if p >= L.last:
        return "Undefined Output"
    return L.elements[p]

def delete(p,L):
    if p >= L.last:
        return "Undefined Output"
    L.elements.pop(p)
    L.elements.append(None)
    L.last -= 1

def nextPosition(p,L):
    if L.last == p:
        return "undefined output"
    return L.elements[p+1]

def previousPosition(p,L):
    if p == 0:
        return "undefined output"
    return L.elements[p-1]

def makeNull(L):
    for i in range (L.last):
        L.elements[i] = None
    L.last = 0
    return end(L)
    
def printarray(L):
    print L.elements[:L.last]
    
def purge(L):
    new_list = []
    new_list = L.elements[:L.last]
    L.elements = list(set(new_list))
    L.last = len(L.elements)
    for i in range (L.last,L.maxsize):
        L.elements.append(None)
        
x = array_list(10)
insert(1,0,x)
insert(2,1,x)
insert(3,2,x)
insert(4,3,x)
insert(5,3,x)
insert(1,1,x)
insert(2,2,x)
printarray(x)
print end(x)
print first(x)
print locate(2,x)
print retrieve(6,x)
print nextPosition(3,x)
print previousPosition(4,x)
printarray(x)
purge(x)
printarray(x)
print x.elements
print endElement(x)







    
