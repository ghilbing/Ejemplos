import math


def allFactors(A):
    # stores the factors of A which are less than square root of A
    # starting from 1 in ascending order
    start_factors = []

    # stores the factors of A which are greater than square root of A
    # starting from A in descending order
    end_factors = []

    for i in range(1, int(A ** (1 / 2.0) + 1)):  # loop from 1 to square root of A
        if A % i == 0:
            start_factors.append(i)
            if i != A ** (1 / 2.0):
                end_factors.append(A / i)  # factors exists in pairs

    end_factors.reverse()  # make end_factors list in ascending order
    start_factors.extend(end_factors)  # combine both lists in start_factors
    return start_factors

A = 85463

print allFactors(A)