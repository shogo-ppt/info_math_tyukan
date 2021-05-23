# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:15:55 2021

@author: legon
"""

import sympy
#from sympy import *

x, y, z, t = sympy.symbols('x y z t')

from sympy.solvers.diophantine.diophantine import diop_linear

print(diop_linear(13*x + 31*y - 1))