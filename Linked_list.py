# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 14:45:55 2016
@author: Shashank Viswanadha
"""
import heap
myHeap = heap.heap(100)
class cell:
    def __init__(self,element):
        self.element = element
        self.next = 0
    
def makeNull():
    header = cell(None)
    myAdd = myHeap.malloc()
    if myAdd != -1:
        myHeap.set_cell(myAdd,header)
    return myAdd
    
def pos(h,y):
    t = myHeap.get_cell(h)
    if t.element == y:
        return h
    else:
        h = t.next
        return pos(h,y)
    
def insert(x,y,h):
    p = pos(h,y)
    currentcell = myHeap.get_cell(p)    
    new_node = cell(x) 
    new_node.next = currentcell.next
    add = myHeap.malloc()  
    if add != -1:
        myHeap.set_cell(add,new_node)
        currentcell.next = add  
    myHeap.set_cell(p,currentcell)
    
def printlist(h):
    while h!= 0:
        node = myHeap.get_cell(h)
        if node.element != None:
            print node.element
        h = node.next
    
header = makeNull()
insert(12,None,header)
insert(11,12,header)
insert(15,11,header)
insert(13,12,header)
printlist(header)

    

    
    
    
    
    
        

    