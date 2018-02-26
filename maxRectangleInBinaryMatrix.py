def maximalRectangle(A):
    if not A or not A[0]:
        return 0
    n = len(A[0])
    height = [0] * (n+1)
    ans = 0
    for row in A:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == 1 else 0
        stack = [-1]
        for i in range(n+1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i -1 - stack[-1]
                ans = max(ans, h*w)
            stack.append(i)
    return ans

A = [[1,1,1],[0,1,1],[1,0,0]]

print maximalRectangle(A)