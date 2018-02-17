from collections import defaultdict

def solve(A):
    if not A:
        return 0
    res = [0 for i in range(len(A))]
    for i in range(1, len(A)):
        res[i] = res[A[i]] + 1
    maxcur = 0
    maxindex = 0
    for i in range(len(res)):
        if res[i] > maxcur:
            maxcur = res[i]
            maxindex = i
    farindex = maxindex
    farparent = A[maxindex]
    counter = 0
    temp = [0 for i in range(len(A))]
    while farindex != 0:
        farindex = farparent
        farparent = A[farindex]
        counter += 1
        temp[farindex] = counter
    for i in range(1, len(A)):
        if temp[i] == 0:
            temp[i] += (temp[A[i]] + 1)
    return max(temp)

A = [ -1, 0, 1, 1, 2, 0, 5, 0, 3, 0, 0, 2, 3, 1, 12, 14, 0, 5, 9, 6, 16, 0, 13, 4, 17, 2, 1, 22, 14, 20, 10, 17, 0, 32, 15, 34, 10, 19, 3, 22, 29, 2, 36, 16, 15, 37, 38, 27, 31, 12, 24, 29, 17, 29, 32, 45, 40, 15, 35, 13, 25, 57, 20, 4, 44, 41, 52, 9, 53, 57, 18, 5, 44, 29, 30, 9, 29, 30, 8, 57, 8, 59, 59, 64, 37, 6, 54, 32, 40, 26, 15, 87, 49, 90, 6, 81, 73, 10, 8, 16 ]

print solve(A)


def solveII(A):
    edge = defaultdict(list)
    for child, parent in enumerate(A):
        if parent != -1:
            edge[parent].append(child)
            edge[child].append(parent)

    answers = [-1, -1]

    def search(start):
        stack = [(start, -1, 0)]
        push, pop = stack.append, stack.pop

        while stack:
            source, previous, distance = pop()

            if distance > answers[0]:
                answers[0], answers[1] = distance, source

            for destination in edge[source]:
                if destination != previous:
                    push((destination, source, distance + 1))

    start = 0
    search(start)

    start = answers[1]
    answers = [-1, -1]
    search(start)

    return answers[0]

print solveII(A)