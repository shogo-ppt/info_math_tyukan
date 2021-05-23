# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:40:11 2021

@author: legon
"""

print('#Nを方とした剰余類')

a = int(input('a:'))
mod = int(input('mod:'))
print()

if a < 0:
    a2 = a + mod
elif a < mod:
    a2 = mod
else:
    a2 = a % mod

print('最小正剰余:',a2)