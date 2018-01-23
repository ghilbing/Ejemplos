def goldStar(A):

    if A == None or len(A) == 0:
        return 0
    stars = len(A)

    #from left to right

    for i in range(0, len(A)):
        if i > 0 and A[i] > A[i-1] or A[i] == A[i-1]:
            stars +=1

    return stars









A = [1, 2, 2, 1, 3, 2]

print goldStar(A)