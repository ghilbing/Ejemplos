def findTheWinner(A):
    game = A[-1]

    n = A[0]
    m = A[0]

    length = len(A)

    arrayA = []
    arrayB = []


    for i in range(0, n):
        arrayA.append(A[i+1])
    for m in range(m+1, length-2):
        arrayB.append(A[m+1])

    if game == 'Even':
        aSum = 0
        bSum = 0
        for i in range(0, len(arrayA)):

            aSum = aSum + arrayA[i] - arrayB[i]
            bSum = bSum + arrayB[i] - arrayA[i]
            i = i + 2

            if aSum > bSum:
                return 'Andrea'
            elif aSum < bSum:
                return 'Maria'
            else:
                return 'Tie'

    else:
        aSum = 0
        bSum = 0
        for j in range(1, len(arrayA)):
            aSum = aSum + arrayA[j] - arrayB[j]
            bSum = bSum + arrayB[j] - arrayA[j]
            j = j + 2

            if aSum > bSum:
                return 'Andrea'
            elif aSum < bSum:
                return 'Maria'
            else:
                return 'Tie'



#A = [3, 1, 2, 3, 3, 3, 2, 1, 'Even']
A = [3, 1, 2, 3, 3, 2, 1, 3, 'Odd']

print findTheWinner(A)
