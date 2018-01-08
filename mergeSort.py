def mergeSort(A):
    print("Splitting ", A)
    if len(A) > 1:
        mid = len(A) // 2
        lefthalf = A[:mid]
        righthalf = A[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        l = 0
        r = 0
        a = 0

        while l < len(lefthalf) and r < len(righthalf):
            if lefthalf[l] < righthalf[r]:
                A[a] = lefthalf[l]
                l += 1
            else:
                A[a] = righthalf[r]
                r += 1
            a += 1

        while l < len(lefthalf):
            A[a] = lefthalf[l]
            l += 1
            a += 1
        while r < len(righthalf):
            A[a] = righthalf[r]
            r += 1
            a += 1
    print("Merging ", A)


A = [54, 26, 93, 17, 77, 32, 44, 55, 20]
mergeSort(A)
print(A)
