# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:00:28 2021

@author: legon
"""

import sympy
import time

print('# ax ≡ 1 (mod n) を、i回繰り返し解く')
a = int(input('a='))
n = int(input('n='))
m = int(input('i='))
print()

#t_list = []
t_sum = 0

if __name__ == '__main__':
    for i in range(0, m):
        start = time.time()
        x,y,t = sympy.gcdex(a,n)
        elapsed_time = time.time() - start
        print('x ≡',x)
        print('elapsed_time:{0}'.format(elapsed_time) + '[sec]')
        print()
        #t_list.append(elapsed_time)
        t_sum += elapsed_time
    print('--------------------')
    # print(t_list)
    print('ave :',t_sum / m)