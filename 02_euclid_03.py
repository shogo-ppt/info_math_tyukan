# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:39:15 2021

@author: legon
"""

import sympy

a_list = []
b_list = []
q_list = []
r_list = []

print('ax + by = (a,b)のを解く')

a = int(input('a : '))
b = int(input('b : '))

print()

c = a
d = b

r = a
i = 0

while r != 0:
    a_list.append(a)
    b_list.append(b)
    q = a // b
    r = a % b
    
    q_list.append(q)
    r_list.append(r)
    
    print('(',i+1,')',a,'=',b,'*',q,'+',r)
    a = b
    b = r
    i += 1

print()
# print(a_list)
# print(b_list)

a,b,c = sympy.gcdex(c,d)
print('x =',a,'t +',b_list[0])
print('y =',b,'t +',a_list[0])
