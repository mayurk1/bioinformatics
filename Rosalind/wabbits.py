#!/usr/bin/env python3
# -*- coding: utf-8 -*-
babies = 0
adults = 1

n = 32
k = 5
i = 1

while i <= n-2:
    newbabies = adults * k
    adults += babies
    babies = newbabies
    i += 1
    
print(babies+adults)
