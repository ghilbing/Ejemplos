def findCount(A, B):
    res = 0
    for i in range(len(A)):
        if B == A[i]:
            res += 1
    return res


def findCountBinarySearch(A, B):
    starting = 0
    ending = 0

    if A[0] == B:
        starting = 0
    else:
        start = 1
        end = len(A) - 1

        while start <= end:
            mid = start + (end - start) / 2

            if A[mid] == B and A[mid - 1] < B:
                starting = mid
                break
            elif A[mid] >= B:
                end = mid - 1
            else:
                start = mid + 1

    if A[-1] == B:
        ending = len(A) - 1 + 1
    else:
        start = 0
        end = len(A) - 2

        while start <= end:
            mid = start + (end - start) / 2

            if A[mid] == B and A[mid + 1] > B:
                ending = mid + 1
                break
            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1

    return ending - starting


A = [1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8]
B = 2

print findCount(A, B)
print findCountBinarySearch(A,B)
