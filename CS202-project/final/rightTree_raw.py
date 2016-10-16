# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:13:08 2016

@author: shashank
"""


class Node():
    #Constructor function. Accepts value of root as input
    #Inputs : 
    #        self : object reference
    #        root_value : Value of the root node
    def __init__(self,root_value):
        self.key = root_value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
    
    #Static Method to create a new Binary Tree.
    #Inputs :
    #      root_value    : Object reference.
    #Returns :
    #       Address of the root node of the newly created binary tree.
    #       
    @staticmethod       # Decorator used to to delare the method as static.The method is static because it creates a new tree with only the root node.
    def createBinaryTree(root_value):
        return Node(root_value)
    
    #Method to locate an element in the binary tree 
    #Inputs :
    #       self      : Object reference.
    #       value     : Key of the element to be located.
    #       stack     : Python list implemented as a stack.Stack used to store nodes which have both left and right children. 
    #Returns :
    #       True  : On success 
    #       False : On failure.If element not found.
    def find(self,value,stack = []):
        if self.key == value:                              # Element found.
            return self
        if self.leftChild != None:                         # If leftChild exists stor current node in stack and go left.
            stack.append(self)
            return self.leftChild.find(value,stack)
        if self.rightChild != None:                        # If righChild exist go right.
            return self.rightChild.find(value,stack)
        else:                                              # If both left and right Children do not exist, pop element from the stack and go to th right of that node.
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
    
    #Method to insert an element to the binary tree 
    #Inputs :
    #       self             : Object reference.
    #       parent_value     : Key of the parent element.The new element should be added as child of this node.
    #       stack            : Key of the new node to be inserted.
    #       pos              : Positon with respect to the parent node where the new node is to be inserted.Default value is left.
    #Returns :
    #       True  : On success 
    #       False : On failure.If element could not inserted.
    def insert(self,parent_value,new_node_value,pos = 'left'):
        parentNode = self.find(parent_value)    # Locating the parent node in the binary tree.
        if parentNode != False:
            if pos == 'left':
                if parentNode.leftChild == None:
                    newNode = Node(new_node_value)
                    parentNode.leftChild = newNode
                    newNode.parent = parentNode
                    return True
                if parentNode.rightChild == None:
                    newNode = Node(new_node_value)
                    parentNode.rightChild = newNode
                    newNode.parent = parentNode
                    return True
                return False
            else:
                if parentNode.rightChild == None:
                    newNode = Node(new_node_value)
                    parentNode.rightChild = newNode
                    newNode.parent = parentNode
                    return True            
        return False
        
    #Method to check if a given node is a leaf.This method is used in the delete method.
    #Inputs :
    #       self      : Object reference.
    #       node     : Address of the node to be checked.
    #Returns :
    #       True  : If given node is a leaf. 
    #       False : If given node is not a leaf.
    def isLeaf(self,node):
        if node.leftChild == None and node.rightChild == None:
            return True
        return False
    
    #Method to find a leaf of the given binary tree.This method is used in the delete method.
    #Inputs :
    #       self      : Object reference.
    #Returns :
    #       The rightmost leaf of the given tree.
    def findLeaf(self):
        if self.rightChild != None:
            return self.rightChild.findLeaf()
        if self.leftChild != None:
            return self.leftChild.findLeaf()
        return self
    
    #Method to check if a given node is a leaf.This method is used in the delete method.If the node to be deleted is an intermediate nod, it is replaced by a leaf of the given tree.This leaf is found usin the findLeaf() meathod.
    #Inputs :
    #       self      : Object reference.
    #       value     : Key of the node to be deleted.
    #Returns :
    #       True  : If given node is a found and deleted. 
    #       False : If given node is not found.
    def delete(self,value):
        node = self.find(value)
        leaf = None
        if node != False:       # Check if the node to be deleted exists.
            if self.isLeaf(node):       # If the node to be deleted is a leaf,delete it directly.
                if node.parent.leftChild == node:
                    node.parent.leftChild = None
                else:
                    node.parent.rightChild = None
                
            else:
                leaf = self.findLeaf()  # If node to be deleted is an intermediate one,find a leaf and replace this node with the leaf.
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
        
    #Method to print the given tree using preOrder traversal.
    #Inputs :
    #       self      : Object reference.
    def preOrder(self):
        if self.key != None:
            print self.key
        if self.leftChild != None:
            (self.leftChild).preOrder()
        if self.rightChild != None:
            (self.rightChild).preOrder()
            
    #Method to convert a given binary tree to a string in the format (Parent(leftChild)(rightChild)).
    #Inputs :
    #       self      : Object reference.
    #       string    : To store the required string built from the given tree.Default value is '' .
    #Returns :
    #       string    : the required representation of the given binary tree.
    def convertToString(self,string = ''):
        string = string + '(' + str(self.key) 
        if self.leftChild == None:
            string = string + '()'
        else:
            string = string  + (self.leftChild).convertToString()
        if self.rightChild == None:
            string = string + '()'
        else:
            string = string + (self.rightChild).convertToString()
        string = string + ')'
        return string
        
    #Method to convert a string in the format (Parent(leftChild)(rightChild))to a binary tree.
    #Inputs :
    #       string    : A string in the format (Parent(leftChild)(rightChild)).
    #Returns :
    #       tree      : the root address of the reqired binary tree constructed using the given string..
    @staticmethod       # Decorator used to to delare the method as static.The method is static because it takes a string as input constructs a binary tree and returns the address the root node.
    def convertToTree(string):
        tree_list = []
        key = ''
        boo = False
        for item in string:
            if item == '(':
                if key != '':
                    tree_list.append(key)
                boo = True
                key = ''
            elif item == ')':
                if boo == True:
                    tree_list.append('.')
                    boo = False
            else:
                key = key + item
        stack = []
        left_right = 0
        tree = None
        for item in tree_list:
            if item == '.':
                left_right +=1
                if left_right == 2:
                    stack.pop()
                    left_right = 1
            else:
                if item == tree_list[0]:
                    tree = Node.createBinaryTree(item)
                    stack.append(tree)
                elif left_right == 0:
                    current_node = stack.pop()
                    stack.append(current_node)
                    tree.insert(current_node.key,item)
                    stack.append(current_node.leftChild)
                elif left_right == 1:
                    current_node = stack.pop()
                    tree.insert(current_node.key,item,'right')
                    stack.append(current_node.rightChild)
                    left_right = 0
                    
        return tree
        
    def encryptTreeToFile(self,name):
        output = open(name,'a')
        print >> output,self.convertToString()

                    
                
            
            
            
            
        
        

"""--------------------Test Cases----------------------------------------------"""  

print '-----------------------------Test Case 1--------------------------\n'

root = Node.createBinaryTree(1)
root.insert(1,2)
root.insert(1,3)
root.insert(2,4)
root.insert(2,5)
root.insert(4,8)
root.insert(5,9)
root.insert(5,10)
root.insert(3,6)
root.insert(3,7)

root.preOrder(),'\n'
te = root.convertToString()
print te,'\n'
fe = Node.convertToTree(te)
fe.preOrder()
print '\n'
print fe.convertToString(),'\n'

print '-----------------------------Test Case 2--------------------------\n'

root1 = Node.createBinaryTree('abc')
root1.insert('abc','b')
root1.insert('abc','e')
root1.insert('b','c')
root1.insert('b','d')
root1.insert('e','f','right')

root1.preOrder(),'\n'
t = root1.convertToString()
print t,'\n'

ro1 = Node.convertToTree(t)
ro1.preOrder()
print '\n'
print ro1.convertToString()


root.encryptTreeToFile('Tree.txt')
fe.encryptTreeToFile('Tree.txt')
root1.encryptTreeToFile('Tree.txt')
ro1.encryptTreeToFile('Tree.txt')