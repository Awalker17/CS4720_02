
def GreedyChangeMaker(D, n):

    F = []
    N = n
    for i in range(len(D)-1, -1, -1):
        while D[i] <= N:
            N -= D[i]
            F.append(D[i])
    return F

D= [1,4,5,9]
n = 30
print(GreedyChangeMaker(D, n))