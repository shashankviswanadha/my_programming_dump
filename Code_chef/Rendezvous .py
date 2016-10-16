# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:23:52 2016

@author: shashank
"""
import sys
nodes = []
keys = []
class tree:
    def __init__(self,key):
        global nodes
        global keys
        self.key = key
        self.leftchild = None
        self.rightchild = None
        self.parent = None
        self.subtreesize = 1
        nodes.append(self)
        keys.append(key)
    
    def kill(self):
        self.key = None
        
        
        
def setchild(node,ch):
    if node.leftchild == None:
        node.leftchild = ch
        ch.parent = node
    else:
        node.rightchild = ch
        ch.parent = node
    x = ch.parent
    while x!= None:
        x.subtreesize += 1
        x = x.parent

    
        
    
T = input()
for i in range (T):
    N = input()
    if N == 1:
        print 1
    else:        
        for i in range (N-1):
            temp = sys.stdin.readline().split()
            if int(temp[0]) not in keys:
                dummy1 = tree(int(temp[0]))
            else:
                for nd in nodes:
                    if nd.key == int(temp[0]):
                        dummy1 = nd
            if int(temp[1]) not in keys:
                dummy2 = tree(int(temp[1]))
            else:
                for nd in nodes:
                    if nd.key == int(temp[1]):
                        dummy2 = nd
            
            setchild(dummy1,dummy2)
        summ = 0
        for k in range (N):
                t = nodes[k].subtreesize
                if nodes[k].subtreesize > 2:
                    summ = summ + (nodes[k].key)*(t*2 + 2*(nodes[k].leftchild.subtreesize) * (nodes[k].rightchild.subtreesize) -1)
                elif nodes[k].subtreesize == 2:
                    summ = summ + (nodes[k].key)*(t*2 + nodes[k].leftchild.subtreesize -1) 
                else:
                    summ = summ + nodes[k].key
                #print summ
        for item in nodes:
            item.kill()
        nodes = []
        keys = []
        print summ
                
            
            
            
            
            
        
        
    
    