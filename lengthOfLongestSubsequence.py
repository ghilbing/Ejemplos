def longestSubsequence(A):
    n = len(A)
    lis = [1 for i in range(n+1)]
    #compute lis values from left to right
    for i in range(1,n):
        for j in range(0, i):
            if (A[i] > A[j]) and (lis[i] < lis[j]+1):
                lis[i] = lis[j] + 1
    lds = [1 for i in range(n+1)]
    #loop from n-2 downto 0
    for i in reversed(range(n-1)):
        #loop from n-1 downto i-1
        for j in reversed(range(i-1, n)):
            if A[i] > A[j] and lds[i] < lds[j]+1:
                lds[i] = lds[j] + 1
    maximum = lis[0] + lds[0] - 1
    for i in range(1, n):
        maximum = max(lis[i] + lds[i]-1, maximum)
    return maximum

A = [1, 11, 2, 10, 4, 5, 2, 1]

print longestSubsequence(A)

#---------------------------------------
m = 0
L = [1] * len(A)
for i in range(1, len(A)):
    for j in range(i):
        if A[j] < A[i]:
            L[i] = max(L[i], L[j] + 1)
R = [1] * len(A)
for i in range(len(A) - 2, -1, -1):
    for j in range(len(A) - 1, i, -1):
        if A[j] < A[i]:
            R[i] = max(R[i], R[j] + 1)
for i in range(len(A)):
    val = L[i] + R[i] - 1
    if val > m:
        m = val
return m

