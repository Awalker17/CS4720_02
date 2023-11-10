
def GreedyChangeMaker(D, n):

    F = []
    N = n
    for i in range(len(D)-1, -1, -1):
        while D[i] <= N:
            N -= D[i]
            F.append(D[i])
    return F

D= [1,2,5,7]
n = 20
for n in range (1, 201):
    print("n=", n, GreedyChangeMaker(D, n), end=", ")