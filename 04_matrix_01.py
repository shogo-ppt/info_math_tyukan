# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:07:45 2021

@author: legon
"""

import sympy

print('Matrix([[a,b],[c,d]]')

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d = int(input('d:'))
mod = int(input('mod:'))
print()

A = sympy.Matrix([[a,b],[c,d]])
A2 = A.det()

# 最小正剰余
if A2 < 0:
    A3 = A2 + mod
elif A2 < mod:
    A3 = mod
else:
    A3 = A2 % mod

print('A =',A) # 行列の表示
A_1 = A.inv()
print('A**(-1) =',A_1) # #逆行列の表示
print()

print('----------------------------------------')
print('#',A3,'x ≡ 1 (mod',mod,')を解く')
print('----------------------------------------')
print('|A| =',A2,'≡',A3,'(mod)',mod) # 
print()

A4 = A2 * A_1
print('A**(-1) ≡',A4,'より')
print()

x,y,t = sympy.gcdex(A3,mod)
A5 = x * A4
a,b,c,d = A5
a %= mod
b %= mod
c %= mod
d %= mod
A6 = sympy.Matrix([[a,b],[c,d]])
print('A**(-1) ≡',x,'*',A4)
print('\t≡',A5)
print('\t≡',A6,'(mod',mod,')')
print()

E = A * A6
a,b,c,d = E
a %= mod
b %= mod
c %= mod
d %= mod
E = sympy.Matrix([[a,b],[c,d]])
print('検算：',A,'*',A6,'≡',E)
