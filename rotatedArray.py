def findRotated(A):
    n = len(A)
    low = 0
    high = n-1
    while low <= high:
        if A[low] <= A[high]:
            return A[low]
        mid = low + (high - low)/2
        nex = (mid+1)%n
        prev = (mid+n-1)%n
        if A[mid]<= A[nex] and A[mid]<= A[prev]:
            return A[mid]
        elif A[mid] <= A[high]:
            high = mid - 1
        elif A[mid] >= A[low]:
            low = mid + 1
    return 0

A = [11, 12, 13, 15, 2, 3, 4, 5, 6, 7, 8, 9]

print findRotated(A)