def largestNumber(A):
    def comp(n1, n2):
        if n1 + n2 > n2 + n1:
            return 1
        elif n1 + n2 < n2 + n1:
            return -1
        else:
            return 0

    string = [str(n) for n in A]
    res = ""

    for n in reversed(sorted(string, cmp=comp)):
        res += n
    result = list(res)
    i = 0
    while result[i] == '0' and i != len(res) - 1:
        i += 1
    result = result[i:]
    return ''.join(result)

A = [3, 30, 34, 5, 9]

print largestNumber(A)