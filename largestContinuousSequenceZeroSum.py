def largestSubsequenceZeroSum(A):
    hash_sum = {}
    max_len = 0
    suma = 0

    for i in range(len(A)):
        suma += A[i]
        if A[i] is 0 and max_len is 0:
            max_len = 1
        if suma is 0:
            max_len = i + 1
        if suma in hash_sum:
            max_len = max(max_len, i - hash_sum[suma])
        else:
            hash_sum[suma] = i
    return max_len

A = [1, -1, 0, 2, -2, 3]

print largestSubsequenceZeroSum(A)

def option2(array):
    seen_sums = dict()
    sm = 0
    strt, end = 0, 0
    seen_sums[0] = 0
    for idx, a in enumerate(array, 1):
        sm += a
        if sm in seen_sums:
            if end - strt < idx - seen_sums[sm]:
                strt, end = seen_sums[sm], idx
        else:
            seen_sums[sm] = idx

    return array[strt:end] if strt != end else []

a = [6,-2,8,5,4,-9,8,-2,1,2]
b = [-8,8]
c = [-7,8,-1]
d = [2200,300,-6,6,5,-9]
e = [-9,9,-6,-3]
f = [1, 2, -3, 3]

print option2(a)
print option2(b)
print option2(c)
print option2(d)
print option2(e)
print option2(f)