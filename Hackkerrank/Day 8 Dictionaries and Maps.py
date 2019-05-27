#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:59:39 2019

@author: xueyi
"""

n = int(input())
phonebook = {}

for _ in range(n):
    names, number = input().split(" ")
    phonebook[names] = number

try:
    while True:            
        name = input()   
        if name == "":      
            break 
        else:
            print(name+"="+phonebook[name] if name in phonebook.keys() else "Not found")
except EOFError:
    pass