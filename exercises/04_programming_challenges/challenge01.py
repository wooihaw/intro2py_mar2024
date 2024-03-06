# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:19:08 2024

@author: wooihaw
"""

# c - Number of chicken
# r - Number of rabbit
# c + r = 35
# 2*c + 4*r = 94

for c in range(36):
    r = 35 - c
    if 2*c + 4*r == 94:
        print(f"There are {c} \N{chicken} and {r} \N{rabbit}.")