from math import factorial
from Functions import *
import logging

'''
for n in range(8, 16):
    numb_items = n
    total = 0
    for i in range(1, numb_items+1):
        total += factorial(numb_items) / (factorial(i) * factorial(numb_items- i))

    print(n, total)
'''
for i in range(15):
    Max, Object = NumbGenerator(15)
    #print(Object)
    greedySerch(Object, Max)

