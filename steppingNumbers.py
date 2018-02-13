def stepnum(self, A, B):
    if B < 10:
        return range(A, B + 1)
    prev = range(1, 10)
    res = []
    if A < 10:
        res.extend(range(A, 10))
    size = len(str(B))
    while True:
        cur = []
        for elem in prev:
            digit = elem % 10
            options = self.options(digit)
            for opt in options:
                num = elem * 10 + opt
                if num > B:
                    return res
                if num >= A:
                    res.append(num)
                cur.append(num)
        prev = cur


def options(self, digit):
    if digit == 0:
        return [digit + 1]
    if digit == 9:
        return [digit - 1]
    else:
        return [digit - 1, digit + 1]

