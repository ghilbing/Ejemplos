def countBits(A):
    ans = 0
    n = len(A)
    for i in range (0,32):
        count = 0
        bitmask = 1 << i
        for num in A:
            if (num & bitmask) != 0:
                count += 1
        ans += (count * (n - count) * 2)
    return ans % (10** 9 + 7)

A = [1,3,6]

print countBits(A)