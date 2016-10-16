# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:33:52 2016

@author: shashank
"""
"""Code contains the transformation of all the functions in Binarytree.py to methods of the BinaryTree class"""
#import Node
class BinaryTree():
    def __init__(self,root_value):
        self.key = root_value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        
    @staticmethod
    def createBinaryTree(root_value):
        return BinaryTree(root_value)
        
    def find(self,value,stack = []):
        if self.key == value:
            return self
        if self.leftChild != None:
            stack.append(self)
            return self.leftChild.find(value,stack)
        else:
            if len(stack)>0:
                next_item = None
                while(len(stack)>0):
                    next_item = stack.pop()
                    if next_item.rightChild != None:
                        break
                    next_item = None
                if stack == [] and next_item == None:
                    return False
                return next_item.rightChild.find(value,stack)           
            stack = []
            return False
            
    def insert(self,parent_value,new_node_value):
        if self.key == parent_value:
            if self.leftChild == None:
                newNode = BinaryTree(new_node_value)
                self.leftChild = newNode
                newNode.parent = self
                return True
            if self.rightChild == None:
                newNode = BinaryTree(new_node_value)
                self.rightChild = newNode
                newNode.parent = self
                return True
            return False
        parentNode = self.find(parent_value)
        if parentNode != False:
            if parentNode.leftChild == None:
                newNode = BinaryTree(new_node_value)
                parentNode.leftChild = newNode
                newNode.parent = parentNode
                return True
            if parentNode.rightChild == None:
                newNode = BinaryTree(new_node_value)
                parentNode.rightChild = newNode
                newNode.parent = parentNode
                return True
            return False 
        return False
        
    def isLeaf(self,node):
        if node.leftChild == None:
            return True
        return False
        
    def findLeaf(self):
        if self.rightChild != None:
            return self.rightChild.findLeaf()
        if self.leftChild != None:
            return self.leftChild.findLeaf()
        return self
        
    def delete(self,value):
        node = self.find(value)
        leaf = None
        if node != False:
            if self.isLeaf(node):
                if node.parent.leftChild == node:
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None
                
            else:
                leaf = self.findLeaf()
                node.key = leaf.key
                if leaf.parent.leftChild == leaf:
                    leaf.parent.leftChild = None
                else:
                    leaf.parent.rightChild = None
            if self.isLeaf(node):
                del(node)
            else:
                del(leaf)
            return True
        return False      
    
    def preOrder(self,stack = []):
        print self.key
        if self.leftChild != None:
            stack.append(self)
            return self.leftChild.preOrder(stack)
        else:
            if len(stack)>0:
                next_item = None
                while(len(stack)>0):
                    next_item = stack.pop()
                    if next_item.rightChild != None:
                        break
                    next_item = None
                if stack == [] and next_item == None:
                    return False
                return next_item.rightChild.preOrder(stack)           
            stack = []
            return False
            
    def convertToString(self,string = ''):
        #print self.key
        string = string + '(' + str(self.key) 
        if self.leftChild == None:
            string = string + '()())'
            return string
        else:
            string = string  + (self.leftChild).convertToString()
            if self.rightChild == None:
                string = string + '())'
                return string
            else:
                string = string + (self.rightChild).convertToString() + ')'
                return string
        string = string + ')'
        return string
            
root = BinaryTree.createBinaryTree(1)
root.insert(1,2)
root.insert(1,3)
root.insert(2,4)
root.insert(2,5)
root.insert(4,8)
root.insert(5,9)
root.insert(5,10)
root.insert(3,6)
root.insert(3,7)
root.insert(6,11)
root.preOrder()
print root.convertToString()
"""print root.insert('a','b')
print root.insert('a','e')
print root.insert('b','c')
print root.insert('b','d')
print root.insert('e','f')
#print root.insert('C','G')
#print root.preOrder()
root.delete('B')
#print root.preOrder()
#print root.leftChild.preOrder()

root1 = BinaryTree.createBinaryTree(1)
root1.insert(1,2)
root1.insert(1,3)
root1.insert(2,4)
root1.insert('F',2)
#print root1.preOrder()
print root.convertToString()
root.preOrder()
root1.preOrder()"""
