#given the list D[1,...m] and the an amount n
#find the mininmum coins required to make the change.


def ChangeMakingAlgo(D, n):
    n += 1
    N = [0]
    for i in range(1, n):
        temp = n * 100
        j = 0
        while (j <= len(D)-1 and i >= D[j]):
            temp = min(N[i - D[j]], temp)
            j += 1
        N.append(temp+1)
    return N[-1]


D= [1,4,5,9]
n = 30
print(ChangeMakingAlgo(D, n))