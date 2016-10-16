# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:32:32 2016

@author: shashank
"""

class BST:
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None
    #@staticmethod
def insert(root,newNode):
        if root == None:
            root = newNode
        else:
            if newNode.key < root.key:
                if root.leftChild == None:
                    root.leftChild = newNode
                    newNode.parent = root
                else:
                    insert(root.leftChild,newNode)
            if newNode.key > root.key:
                if root.rightChild == None:
                    root.rightChild = newNode
                    newNode.parent = root
                else:
                    insert(root.rightChild,newNode)
    #@staticmethod
def findMin(tree):
        if tree.leftChild == None:
            print tree.leftChild
            return tree.parent.key
            
        else: 
            print tree.leftChild
            findMin(tree.leftChild)

tree = BST(40)
insert(tree,BST(35))
insert(tree,BST(4))
print tree.leftChild.key
print tree.leftChild.leftChild.key
print tree.leftChild.parent.key
print findMin(tree)
            