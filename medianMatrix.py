def findMedian(A):
    for i in range(1,len(A)):
        A[0].extend(A[i])
        A[i] = None
    A = sorted(A[0])
    return A[len(A)//2]



A = [[1, 3, 5],
[2, 6, 9],
[3, 6, 9]]

print findMedian(A)

