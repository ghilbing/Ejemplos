def maximumAbsoluteDifference(A):
    if not A:
        return 0
    else:
        N = len(A)
        mx1, mx2, mx3, mx4 = [-10 ** 15] * 4
        for i in range(N):
            mx1 = max(mx1, A[i] + i)
            mx2 = max(mx2, - A[i] + i)
            mx3 = max(mx3, A[i] - i)
            mx4 = max(mx4, -A[i] - i)
        ans = -10 ** 15
        for i in range(N):
            ans = max(ans, mx1 - A[i] - i);
            ans = max(ans, mx2 + A[i] - i);
            ans = max(ans, mx3 - A[i] + i);
            ans = max(ans, mx4 + A[i] + i);
        return ans


A = [1, 3, -1]

def maxAbsoluteDifference(A):
    result = 0
    first = [A[i] + i for i in range(len(A))]
    second = [A[i] - i for i in range(len(A))]
    first_min, first_max = min(first), max(first)
    second_min, second_max = min(second), max(second)
    return max(first_max - first_min, second_max - second_min)


print maximumAbsoluteDifference(A)
print maxAbsoluteDifference(A)