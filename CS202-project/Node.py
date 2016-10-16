# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:32:00 2016

@author: shashank
"""
"""Class Node"""
class Node():
    def __init__(self,value):
        self.key = value
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        