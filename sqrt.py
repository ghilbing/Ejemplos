def sqrt(A):
    if A == 0:
        return 0
    start = 1
    end = A
    res = 0
    while start <= end:
        mid = start + (end - start)//2
        sqr = mid * mid
        if sqr < A:
            res = max(res, mid)
            start = mid + 1
        elif sqr > A:
                end = mid - 1
        else:
            return mid

    return res

A = 27

print sqrt(A)