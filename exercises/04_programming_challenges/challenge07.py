# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:58:03 2024

@author: wooihaw
"""

from collections import Counter

with open("data/alice.txt", "r") as f:
    s = f.read()
    t = [c.lower() if c.isalpha() else ' ' for c in s]
    u = ''.join(t)
    w = u.split()
    # print(w)
    c = Counter(w)
    print(f"Total number of unique words: {len(c)}")
    print(f"Top ten most frequently words: {c.most_common(10)}")
    print(f"The word 'alice' appears {c['alice']} times.")