# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:49:22 2016

@author: shashank
"""
""" Initial construction of the Binary Tree ADT"""
class BinaryTree:
    def __init__(self,value):
        self.key = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        
def createBinaryTree(root_value):
    return BinaryTree(root_value)

def find(value,root,stack = []):
    if root.key == value:
        return root
    if root.leftChild != None:
        stack.append(root)
        return find(value,root.leftChild,stack)
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
            return find(value,next_item.rightChild,stack)           
        stack = []
        return False
        
def insert(parent_value,new_node_value,root_node,pos = 'left'):
    """if root_node.key == parent_value:
        if root_node.leftChild == None:
            newNode = BinaryTree(new_node_value)
            root_node.leftChild = newNode
            newNode.parent = root_node
            return True
        if root_node.rightChild == None:
            newNode = BinaryTree(new_node_value)
            root_node.rightChild = newNode
            newNode.parent = root_node
            return True
        return False"""
    parentNode = find(parent_value,root_node)
    if parentNode != False:
        if pos == 'left':
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
        else:
            if parentNode.rightChild == None:
                newNode = BinaryTree(new_node_value)
                parentNode.rightChild = newNode
                newNode.parent = parentNode
                return True            
    return False
    
def isLeaf(node):
    if node.leftChild == None:
        return True
    return False

def findLeaf(root):
    if root.rightChild != None:
        return findLeaf(root.rightChild)
    if root.leftChild != None:
        return findLeaf(root.leftChild)
    return root
    
def delete(value,root):
    node = find(value,root)
    leaf = None
    if node != False:
        if isLeaf(node):
            if node.parent.leftChild == node:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
            
        else:
            leaf = findLeaf(root)
            node.key = leaf.key
            if leaf.parent.leftChild == leaf:
                leaf.parent.leftChild = None
            else:
                leaf.parent.rightChild = None
        if isLeaf(node):
            del(node)
        else:
            del(leaf)
        return True
    return False            
            
def preOrder(root,stack = []):
    print root.key
    if root.leftChild != None:
        stack.append(root)
        return preOrder(root.leftChild,stack)
    #if root.rightChild != None:
     #       return preOrder(root.rightChild,stack)
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
            return preOrder(next_item.rightChild,stack)           
        stack = []
        return False
        
root = createBinaryTree('A')
print insert('A','B',root)
print insert('A','C',root)
print insert('B','D',root)
print insert('B','E',root)
print insert('C','F',root)
print insert('C','G',root)
print insert('G','Z',root)
print insert('G','H',root)#,'right')
print preOrder(root)
print find ('G',root).rightChild.key
#delete(2,root)
#print preOrder(root)



    
        
    