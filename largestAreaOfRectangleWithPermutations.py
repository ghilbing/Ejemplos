def solve(A):
    if not A:
        return 0
    rows = len(A)
    cols = len(A[0])
    hist = [[0 for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        hist[0][j] = A[0][j]
        for i in range(1, rows):
            if A[i][j] == 1:
                hist[i][j] = hist[i - 1][j] + 1
    for row in hist:
        row.sort(reverse=True)
    max_area = float('-inf')
    for i in range(rows):
        for j in range(cols):
            curr_area = (j + 1) * hist[i][j]
            max_area = max(max_area, curr_area)
    return max_area


A = [[1,0,1],[0,0,1],[1,0,0]]
print solve(A)