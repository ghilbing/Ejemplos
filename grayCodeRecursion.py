def grayCode(A):
    results = [0]
    for i in range(A):
        results += [x + pow(2, i) for x in reversed(results)]
    return results

A = 3

print grayCode(A)

def grayCodeII(A):
    res = [0]
    for i in range(A):
        t = 1 << i
        temp = [j+t for j in reversed(res)]
        res = res + temp
    return res

print grayCodeII(A)