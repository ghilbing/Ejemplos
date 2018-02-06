def findMedianSortedArrays(A, B):
    a = len(A)
    b = len(B)
    if a > b:
        return findMedianSortedArrays(B, A)
    if b == 0:
        raise ValueError
    imin = 0
    imax = a
    mid = (a + b + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = mid - i
        if i < a and B[j - 1] > A[i]:
            imin = i + 1
        elif i > 0 and A[i - 1] > B[j]:
            imax = i - 1
        else:
            if i == 0:
                maxLeft = B[j - 1]
            elif j == 0:
                maxLeft = A[i - 1]
            else:
                maxLeft = max(A[i - 1], B[j - 1])
            if (a + b) % 2 == 1:
                return maxLeft

            if i == a:
                minRight = B[j]
            elif j == b:
                minRight = A[i]
            else:
                minRight = min(A[i], B[j])
            return (maxLeft + minRight) / float(2)


#A = [-50, -41, -40, -19, 5, 21, 28]
#B = [-50, -21, -10]

A = [0, 23]
B = []

print findMedianSortedArrays(A, B)
