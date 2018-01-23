def colorfullNumber(A):
    N = str(A)
    vals = set()
    for l in range(1, len(N) + 1):
        for i in range(0, len(N) - l + 1):
            ans = 1
            for k in range(i, i + l):
                ans *= int(N[k])
            if ans in vals:
                return 0
            vals.add(ans)
    return 1

A = "3245"

print colorfullNumber(A)
