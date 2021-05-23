# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:15:57 2021

@author: legon
"""

q_list = []
r_list = []

a = int(input('a='))
b = int(input('b='))

r = a
i = 0

while r != 0:
    q = a // b
    r = a % b
    
    q_list.append(q)
    r_list.append(r)
    
    print('(',i,')',a,'=',b,'*',q,'+',r)
    a = b
    b = r
    i += 1
print('GCD=',a)
print()
print(q_list)
print(r_list)

