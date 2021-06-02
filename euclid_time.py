# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 19:15:14 2021

@author: legon
"""

import time

print('ax + by = (a,b)のを解く')

a = int(input('a : '))
b = int(input('b : '))

r = a
i = 0

print()

if __name__ == '__main__':
    start = time.time()
    
    # 計測する処理内容
    while r != 0:
        q = a // b
        r = a % b
        
        print('(',i+1,')',a,'=',b,'*',q,'+',r)
        a = b
        b = r
        i += 1
    # ここまで

    elapsed_time = time.time() - start
    print('elapsed_time:{0}'.format(elapsed_time) + '[sec]')
    print()
    print('GCD=',a)