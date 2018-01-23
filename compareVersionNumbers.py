def compareVersionNumbers(A,B):
    version1, version2 = len(A), len(B)
    i, j = 0, 0
    while i < version1 or j < version2:
        v1, v2 = 0, 0
        while i < version1 and A[i] != ".":
            v1 = v1 * 10 + int(A[i])
            i +=1
        while j < version2 and B[j] != ".":
            v2 = v2 * 10 + int(B[j])
            j +=1
        if v1 != v2:
            return 1 if v1 > v2 else -1
        i +=1
        j +=1

    return 0


A = [10.4]
B = [1.0]



print compareVersionNumbers(A, B)





