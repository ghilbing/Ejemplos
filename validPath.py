def validPath(A, B, C, D, E, F):
    top = B
    bottom = 0
    left = 0
    right = A
    num = C
    R = D
    circles = {}
    topSet = {}
    bottomSet = {}
    leftSet = {}
    rightSet = {}
    for i in range(num):
        center = (E[i], F[i])
        circles[center] = {}
    for i in range(num):
        center = (E[i], F[i])
        if E[i] - R <= left and F[i]-R <= bottom:
            return "No"
        if E[i] + R >= right and F[i]+R >= top:
            return "No"
        if E[i] - R <= left:
            leftSet[center] = 1
        if E[i] + R >= right:
            rightSet[center] = 1
            if center in leftSet:
                return "No"
        if F[i] - R <= bottom:
            bottomSet[center] = 1
        if F[i] + R >= top:
            topSet[center] = 1
            if center in bottomSet:
                return "No"
        for j in range(i+1, num):
            if i == j:
                continue
            center2 = (E[j], F[j])
            d = (E[i]- E[j])**2 + (F[i]- F[j])**2
            r = (R*2)**2
            if 0 <= d and d<= r:
                circles[center][center2] = 1
                circles[center2][center] = 1
    if len(topSet) == 0 and len(bottomSet) == 0 and len(leftSet) == 0 and len(rightSet) == 0:
        return "Yes"
    visited = {}
    myQ = []
    for c in topSet:
        if c in visited:
            continue
        myQ.append(c)
        visited[c] = 1
        while(len(myQ)> 0):
            v = myQ[0]
            del myQ[0]
            for n in circles[v]:
                if n in visited:
                    continue
                visited[n] = 1
                myQ.append(n)
                if n in rightSet or n in bottomSet:
                    return "No"
    myQ = []
    for c in leftSet:
        if c in visited:
            continue
        myQ.append(c)
        visited[c] = 1
        while len(myQ)> 0:
            v = myQ[0]
            del myQ[0]
            for n in circles[v]:
                if n in visited:
                    continue
                visited[n] = 1
                myQ.append(n)
                if n in rightSet or n in bottomSet:
                    return "No"
    return "Yes"


A = 10
B = 8
C = 2
D = 1
E = [2,8]
F = [3,5]

print validPath(A, B, C, D, E, F)
