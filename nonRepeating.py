def nonRepeating(A):
    dictionary = {}
    for c in A:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1
    for c in A:
        if dictionary[c] == 1:
            return c
    return None


A = "aabbdbc"

print nonRepeating(A)