# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 23:37:38 2016

@author: shashank
"""

import heap
myHeap = heap.heap(100)

class Stack():
    def __init__(self,element):
        self.element = element
        self.next = None
        
def makeNull():
    add = myHeap.malloc()
    if add != -1:
        myHeap.set_cell(add,Stack(None))
        return add
    return False
    
def getLast(header):
    cell = myHeap.get_cell(header)
    if cell.next == None:
        return header
    return getLast(cell.next)
    
def getPenultimate(header):
    cell = myHeap.get_cell(header)
    if cell.next == None:
        return False
    else:
        if myHeap.get_cell(cell.next).next == None:
            return header
        else:
            return getPenultimate(cell.next)
            
def push(value,header):
    current_add = getLast(header)
    current_cell = myHeap.get_cell(current_add)
    new_add = myHeap.malloc()
    if new_add != -1:
        myHeap.set_cell(new_add,Stack(value))
        current_cell.next = new_add
        myHeap.set_cell(current_add,current_cell)
        return True
    return False

def pop(header):
    penul_add = getPenultimate(header)
    if penul_add == False:
        print "No elements to pop"
        return False
    else:
        penul_cell = myHeap.get_cell(penul_add)
        print myHeap.get_cell(penul_cell.next).element
        penul_cell.next = None
        return True
        
def printStack(header):
    cell = myHeap.get_cell(header)
    if cell.element != None:
        print cell.elemnet
        if cell.next != None:
            printStack(cell.next)
            

head = makeNull()
push(1,head) 
push(2,head) 
pop(head)
pop(head) 
pop(head)   
        