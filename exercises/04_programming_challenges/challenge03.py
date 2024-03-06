# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:33:42 2024

@author: wooihaw
"""

s1 = set(range(1, 101))
s2 = set(range(5, 101, 5))
s3 = set(range(7, 101, 7))

result = s1 - (s2 | s3)
print(result)
