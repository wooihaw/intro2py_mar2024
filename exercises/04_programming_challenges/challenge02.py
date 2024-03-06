# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:25:15 2024

@author: wooihaw
"""

try:
    investment = float(input("Enter the initial investment: "))
    rate = float(input("Enter the annual rate (%): "))
    years = int(input("Enter years of investment: "))
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Initial investment: RM{investment}, annual rate: {rate}%, years of investment: {years}")
    for y in range(years):
        investment = investment + investment * rate/100
        print(f"Year {y+1}: RM{investment:.2f}")