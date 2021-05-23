# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:15:57 2021

@author: legon
"""

a_list = []
b_list = []
q_list = []
r_list = []

a = int(input('a='))
b = int(input('b='))

r = a
i = 0

print()
while r != 0:
    a_list.append(a)
    b_list.append(b)
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
print('a_list:',a_list)
print('b_list:',b_list)
print('q_list:',q_list)
print('r_list:',r_list)
print()

l = len(a_list) - 1

i = 1

"""
temp = j + q_list[l-i+1] * q_list[l-i]
"""

while l-i+1 != 0:
    print('=',a_list[l-i],'+',b_list[l-i])
    i += 1
