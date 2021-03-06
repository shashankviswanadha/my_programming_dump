# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 23:59:51 2016

@author: shashank
"""

import heap
myHeap = heap.heap(100)

class Queue():
    def __init__(self,element):
        self.element = element
        self.next = None
        
def makeNull():
    add = myHeap.malloc()
    if add != -1:
        myHeap.set_cell(add,Queue(None))
        return add
    return False
    
def getLast(header):
    cell = myHeap.get_cell(header)
    if cell.next == None:
        return header
    return getLast(cell.next)
    
def push(value,header):
    current_add = getLast(header)
    current_cell = myHeap.get_cell(current_add)
    new_add = myHeap.malloc()
    if new_add != -1:
        myHeap.set_cell(new_add,Queue(value))
        current_cell.next = new_add
        myHeap.set_cell(current_add,current_cell)
        return True
    return False
def checkLen1(header):
    if myHeap.get_cell(myHeap.get_cell(header).next).next == None:
        return True
    else:
        return False
    
def pop(header):
    cell = myHeap.get_cell(header)
    if cell.next == None:
        print "No elements to pop"
        return False
    else:
        if checkLen1(header):
            print myHeap.get_cell(myHeap.get_cell(header).next).element
            myHeap.get_cell(header).next = None
        else:
            newFirst_add = myHeap.get_cell(myHeap.get_cell(header).next).next
            print myHeap.get_cell(myHeap.get_cell(header).next).element
            myHeap.get_cell(header).next = newFirst_add
        return True
        
head = makeNull()
push(1,head) 
push(2,head) 
pop(head)
pop(head) 
pop(head)   
            
            
        
