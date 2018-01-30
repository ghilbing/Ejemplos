def searchMatrix(A, B):
    y = len(A)
    x = len(A[0])
    start = 0
    end = x * y - 1
    while start <= end:
        mid = start + (end - start) // 2
        if A[mid // x][mid % x] == B:
            return 1
        elif A[mid // x][mid % x] < B:
            start = mid + 1
        else:
            end = mid - 1
    return 0

A = [[1,   3,  5,  7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]
B = 16


def anotherOption(A, B):
    def binarySearch(matrix):
        low = 0
        high = len(matrix) -1
        while low <= high:
            mid = low + (high - low)/2
            if matrix[mid] == B:
                return 1
            elif matrix[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        return 0

    for x in A:
        if x[-1] >= B:
            return binarySearch(x)

print searchMatrix(A, B)
print anotherOption(A, B)
