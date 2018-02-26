def adjancent(A):
    if len(A) == 0:
        return 0

    inc = 0
    exc = 0

    for i in range(len(A[0])):
        maxm = max(A[0][i], A[1][i])
        temp = inc
        inc = max(inc, exc + maxm)
        exc = temp
    return inc

A = [[1,2,3,4],[2,3,4,5]]

print adjancent(A)