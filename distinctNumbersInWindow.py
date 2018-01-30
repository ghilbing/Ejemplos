def dNums(A, B):
    numberMap = {}
    count = 0
    ptr = -1
    res = []
    if B > len(A):
        return res
    else:
        for i in range(0, len(A)):
            if numberMap.get(A[i], 0) == 0:
                count += 1
                numberMap[A[i]] = 1
            else:
                numberMap[A[i]] += 1
            if i >= B:
                ptr += 1
                numberMap[A[ptr]] -= 1
                if numberMap[A[ptr]] == 0:
                    count -= 1
            if i >= B - 1:
                res.append(count)
    return res


def dNumsII(A, B):
    length = len(A)
    if B > length:
        return []
    if B == 0:
        return A
    i = 0
    dic = {}
    ans = []
    for j in range(B):
        if A[j] in dic:
            dic[A[j]] += 1
        else:
            dic[A[j]] = 1
    ans.append(len(dic))
    j = B
    while j < length:
        dic[A[i]] -= 1
        if dic[A[i]] == 0:
            del dic[A[i]]

        if A[j] in dic:
            dic[A[j]] += 1
        else:
            dic[A[j]] = 1
        i += 1
        j += 1

        ans.append(len(dic))

    return ans


A = [1, 2, 1, 3, 4, 3]
B = 3

print dNums(A, B)
print dNumsII(A, B)
