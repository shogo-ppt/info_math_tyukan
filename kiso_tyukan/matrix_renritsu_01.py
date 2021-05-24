# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:07:45 2021

@author: legon
"""

import sympy

print('--------------------------------------------------')
print('# [[a,b],[c,d]]*[x,y]≡[e,f] mod(?)となる[x,y]を求める')
print('--------------------------------------------------')

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d = int(input('d:'))
e = int(input('e:'))
f = int(input('f:'))
mod = int(input('mod:'))
print()

A = sympy.Matrix([[a,b],[c,d]])
A2 = A.det()

# 最小正剰余
A3 = A2 % mod
"""
if A2 < 0:
    A3 = A2 + mod
elif A2 < mod:
    A3 = mod
else:
    A3 = A2 % mod
"""

# 行列の表示
print('A =')
print('[',a,',',b,']')
print('[',c,',',d,']')
print()

A_1 = A.inv()
# 逆行列の表示
print('A**(-1) =')
a,b,c,d = A_1
print('[',a,',',b,']')
print('[',c,',',d,']')
print()

print('--------------------------------------------------')
print('#',A3,'x ≡ 1 (mod',mod,')を解く')
print('--------------------------------------------------')
print()
print('|A| =',A2,'≡',A3,'(mod)',mod) # 
print()

A4 = A2 * A_1
# 逆行列の表示
print('A**(-1) ≡より')
a,b,c,d = A4
print('[',a,',',b,']')
print('[',c,',',d,']')
print()

x,y,t = sympy.gcdex(A3,mod)
A5 = x * A4

print('A**(-1) ≡',x,'*')
print('[',a,',',b,']')
print('[',c,',',d,']')
print('≡')
a,b,c,d = A5
print('[',a,',',b,']')
print('[',c,',',d,']')
print('≡')
# a,b,c,d = A5
a %= mod
b %= mod
c %= mod
d %= mod

# A6:求める逆行列
A6 = sympy.Matrix([[a,b],[c,d]])
a,b,c,d = A6
print('[',a,',',b,']')
print('[',c,',',d,'] (mod',mod,')')
print()

print('よって、求める逆行列は、')
print('[',a,',',b,']')
print('[',c,',',d,'] (mod',mod,')')
print()

"""
E = A * A6
a,b,c,d = E
a %= mod
b %= mod
c %= mod
d %= mod
E = sympy.Matrix([[a,b],[c,d]])
print('検算：',A,'*',A6,'≡',E)
"""

print('求めるx,yは、')
B1 = sympy.Matrix([e,f])
B2 = A6 * B1
# print(B2)
print('[ x ]')
print('[ y ]')
print('≡')
print('[',a,',',b,']')
print('[',c,',',d,']')
print('*')
print('[',e,']')
print('[',f,']')

a,b = B2
a %= mod
b %= mod
B3 = sympy.Matrix([a,b])
# print(B3)

print('≡')
print('[',a,']')
print('[',b,'] mod(',mod,')')
