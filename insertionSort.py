def insertionSort(A):
    for i in range(1, len(A)):

        currentvalue = A[i]
        position = i

        while position > 0 and A[position - 1] > currentvalue:
            A[position] = A[position - 1]
            position = position - 1

        A[position] = currentvalue


A = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(A)
print(A)
