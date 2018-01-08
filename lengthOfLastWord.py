def lengthOfLastWord(A):
    length = 0
    for i in reversed(A):
        if i == ' ':
            if length:
                break
        else:
            length += 1
    return length


def spliting(A):
    n = A.split()
    if len(n) == 0:
        return 0
    else:
        return len(n[-1])


A = "Hello World!"
print lengthOfLastWord(A)
print spliting(A)
