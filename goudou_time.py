# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:00:28 2021

@author: legon
"""

import sympy
import time

print('# ax ≡ 1 (mod n) を解く')
a = int(input('a='))
n = int(input('n='))

if __name__ == '__main__':
    start = time.time()
    
    # 計測する処理内容
    x,y,t = sympy.gcdex(a,n)
    # ここまで
    
    elapsed_time = time.time() - start
    print('elapsed_time:{0}'.format(elapsed_time) + '[sec]')
    print('--------------------')
    print('x ≡',x)