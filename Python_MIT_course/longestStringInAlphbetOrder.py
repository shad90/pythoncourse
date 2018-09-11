# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
s = input("Input String Here: ")
max_str = ''
temp_str = ''
for l in s:
    if len(temp_str) == 0:
        temp_str=l
    elif (l >= temp_str[-1]):
        temp_str += l
    else:
        temp_str = l
    if len(max_str) < len(temp_str):
        max_str = temp_str
#        temp_str = l
#    else:
#        temp_str = l
        
print("Longest substring in alphabetical order is:",max_str)
