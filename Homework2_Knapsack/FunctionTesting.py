'''
This code does not affect the functionality of the program.
Change anything.
'''

from math import factorial
from Functions import *
import logging
from Plot_Results import *

# use # on disable line to enable debug print statements
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

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

