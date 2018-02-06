import heapq
def solve(A, B):
    queue = []
    A = list(reversed(sorted(A)))
    B = list(reversed(sorted(B)))
    def push(i, j):
        if i < len(A) and j < len(B):
            heapq.heappush(queue, [-(A[i] + B[j]), i, j])
    push(0,0)
    res = []
    while queue and len(res) < len(A):
        _, i, j = heapq.heappop(queue)
        res.append(A[i] + B[j])
        push(i, j+ 1)
        if j == 0:
            push(i + 1, 0)

    return res


A = [1, 4, 2, 3]
B = [2, 5, 1, 6]

print solve(A, B)
