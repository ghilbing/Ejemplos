import heapq
def chocolates(A, B):
    queue = []
    def check(queue, A):
        ans = 0
        div = pow(10, 9)+ 7
        while A:
            top = queue(0)
            ans = (ans + (top%div))%div

            heapq.heappop()
            heapq.heappush(top/2)

            A -= 1
        return ans
    if len(B) == 0:
        return 0
    for i in range(len(B)):
        heapq.heappush(B[i])

    return check(queue, A)

A = [6, 5]
B = [2]

print chocolates(A, B)
