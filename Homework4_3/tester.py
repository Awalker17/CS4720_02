from greedy import *
from changeMaker import *

D= [1,4,5,9]
D= [1,10,15,21]
D = [1,3,6,7]

Original = []
Greedy = []
Competitive = []
for n in range(1,1000):
    a = ChangeMakingAlgo(D, n)
    b = len(GreedyChangeMaker(D, n))
    Competitive.append(a/b)

print(Competitive)



