# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 12:46:34 2016

@author: shashank
"""

class priorityQ():
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.array = [None for i in range(self.maxSize)]
        self.arrayPointer = 0
        
def makeNull(maxSize):
    return priorityQ(maxSize)
    
def swapInsert(PQ,point = None):
    if point == None:
        point = PQ.arrayPointer
    parent = point/2
    if PQ.array[point - 1] < PQ.array[parent - 1]:
        PQ.array[point - 1],PQ.array[parent - 1] = PQ.array[parent - 1],PQ.array[point - 1]
        swapInsert(PQ,parent)
    
def insert(value,PQ):
    PQ.arrayPointer += 1
    PQ.array[PQ.arrayPointer - 1] = value
    swapInsert(PQ)
    
def swapDelete(PQ,point = 1):
    leftChild = 2*point
    rightChild = leftChild + 1
    if PQ.array[rightChild - 1] != None:
        if PQ.array[leftChild - 1] < PQ.array[point - 1] and PQ.array[rightChild - 1] > PQ.array[point - 1]:
            PQ.array[point - 1],PQ.array[leftChild - 1] = PQ.array[leftChild - 1],PQ.array[point - 1]
            swapDelete(PQ,leftChild - 1)
        elif PQ.array[rightChild - 1] < PQ.array[point - 1] and PQ.array[leftChild - 1] > PQ.array[point - 1]:
            PQ.array[point - 1],PQ.array[rightChild - 1] = PQ.array[rightChild - 1],PQ.array[point - 1]
            swapDelete(PQ,rightChild - 1)
        elif PQ.array[leftChild - 1] < PQ.array[point - 1] and PQ.array[rightChild - 1] < PQ.array[point - 1]:
            if PQ.array[leftChild - 1] < PQ.array[rightChild - 1]:
                PQ.array[point - 1],PQ.array[leftChild - 1] = PQ.array[leftChild - 1],PQ.array[point - 1]
                swapDelete(PQ,leftChild -1)
            elif PQ.array[rightChild - 1] < PQ.array[leftChild - 1]:
                PQ.array[point - 1],PQ.array[rightChild - 1] = PQ.array[rightChild - 1],PQ.array[point - 1]
                swapDelete(PQ,rightChild -1)
                
    elif PQ.array[leftChild - 1] != None and PQ.array[rightChild - 1] == None:
        if PQ.array[leftChild - 1] < PQ.array[point - 1]:
            PQ.array[point - 1],PQ.array[leftChild - 1] = PQ.array[leftChild - 1],PQ.array[point - 1]
            
    
            
        
    
    
    
def deleteMin(PQ):
    PQ.array[0] = PQ.array[PQ.arrayPointer - 1]
    PQ.array[PQ.arrayPointer - 1] = None
    PQ.arrayPointer -= 1
    swapDelete(PQ)
    
def printPriorityQ(PQ):
    for x in PQ.array:
        if x == None:
            break
        print x
    
    
    
r = makeNull(10)
insert(5,r)
insert(4,r)
insert(9,r)
insert(3,r)
insert(2,r)
insert(1,r)
insert(6,r)
deleteMin(r)
deleteMin(r)
deleteMin(r)
deleteMin(r)
deleteMin(r)
deleteMin(r)
#deleteMin(r)
printPriorityQ(r)
    
    
    
    
        