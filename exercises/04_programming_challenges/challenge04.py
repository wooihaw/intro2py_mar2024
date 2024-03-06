# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:37:36 2024

@author: wooihaw
"""

def mean(data):
    return sum(data)/len(data)

def median(data):
    n = len(data)
    if n%2:
        return data[n//2]
    else:
        return (data[n//2 - 1] + data[n//2]) / 2

with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()
    # print(raw_data)
    data = [float(t.strip()) for t in raw_data]
    # print(data)
    data.sort()
    print(f"Lowest: {data[0]}, highest: {data[-1]}")
    print(f"Mean: {mean(data)}, median: {median(data)}")
    