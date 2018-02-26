import math


def numTrees(A):
    trees = [0] * (A+1)
    trees[0] = 1
    for i in range(1, A+1):
        for j in range(i):
            trees[i] += trees[j] * trees[i-1-j]
    return trees[A]

A = 7

print numTrees(A)

#Catalan Number
# (2n)!/((n+1)!*n!

def numTreesCatalan(A):
    return math.factorial(2*A)/(math.factorial(A)*math.factorial(A+1))

print numTreesCatalan(A)