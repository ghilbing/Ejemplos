def nQueen(n):

    def dfs(queens, xy_dif, xy_sum):
        l = len(queens)
        if l == n:
            res.append(queens)
            return None
        for q in range(n):
            if q not in queens and l - q not in xy_dif and l + q not in xy_sum:
                dfs(queens + [q], xy_dif + [l - q], xy_sum + [l + q])

    res = []
    dfs([], [], [])
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in res]


n = 4

print nQueen(n)
