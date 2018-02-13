def solve(A, B, C, D):
    dic = {}
    ans = []
    dic[A] = dic[B] = dic[C] = 1
    for i in range(D):
        val = min(dic)
        ans.append(val)
        del dic[val]
        dic[val * A] = dic[val * B] = dic[val * C] = 1
    return ans

A = 2
B = 3
C = 5
D = 5

print solve(A,B,C,D)