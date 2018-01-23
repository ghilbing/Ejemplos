def repeatedAndMissingNunber(A):
    arr = [0 for x in range(len(A))]
    for i in range(len(A)):
        arr[A[i] - 1] += 1
    for j in range(len(arr)):
        if arr[j] > 1:
            repeated = j + 1
        if arr[j] == 0:
            missing = j + 1
    return [repeated, missing]

#sin memoria extra

def repeatedAndMissing(A):
    n = len(A)
    x = sum(range(1, n+1))-sum(A)
    y = sum([i**2 for i in range(1, n+1)])-sum([i**2 for i in A])
    b=((x**2) + y)//(2*x)
    a=(y-(x**2))//(2*x)

    return a,b



A = [1,2,3,4,5,5]

print repeatedAndMissingNunber(A)
print repeatedAndMissing(A)