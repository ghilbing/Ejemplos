def bubbleSort(A):
    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp


A = [54, 26, 17, 77, 31, 44, 55, 20]
bubbleSort(A)
print (A)
