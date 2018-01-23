def removeDuplicates(A):
    if not A:
        return 0
    tail = 0
    for i in range(1, len(A)):
        if A[i] != A[tail]:
            tail +=1
            A[tail] = A[i]
    return tail + 1

A = [2,3,5,5,7,11,11,11,11,13]

def removeDupl(A):
    i = 0
    while i < (len(A) -1):
        if A[i] is A[i + 1]:
            del A[i]
        else:
            i +=1
    return len(A)

print removeDuplicates(A)
print removeDupl(A)