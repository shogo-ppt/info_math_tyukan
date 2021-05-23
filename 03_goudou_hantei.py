# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:44:31 2021

@author: legon
"""

print('a ≡ b の判定')

a = int(input('a : '))
b = int(input('b : '))
N = int(input('N : '))

print()
print('a % N =',a % N)
print('b % N =',b % N)
print()

if a % N == b % N:
    print('true')
else:
    print('false')