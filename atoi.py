def myAtoi(A):
    INT_MAX = 2 ** 31-1
    INT_MIN = -2 ** 31
    result = 0

    if not A:
        return result

    i = 0
    while i < len(A) and A[i].isspace():
        i +=1

    sign = 1
    if A[i] == "+":
        i +=1
    elif A[i] =="-":
        sign = -1
        i +=1

    while i < len(A) and '0' <= A[i] <= '9':
        if result > (INT_MAX - int(A[i]))/ 10:
            return INT_MAX if sign >0 else INT_MIN
        result = result * 10 + int(A[i])
        i +=1
    return sign * result

A = "-134 Ab"


def atoi(A):
    A = A.strip()  # strips all spaces on left and right
    if not A: return 0
    sign = -1 if A[0] == '-' else 1
    val, index = 0, 0
    if A[0] in ['+', '-']: index = 1
    while index < len(A) and A[index].isdigit():
        val = val * 10 + ord(A[index]) - ord('0')  # assumes there're no invalid chars in given string
        index += 1
    # return sign*val
    return max(-2 ** 31, min(sign * val, 2 ** 31 - 1))

print atoi(A)
print myAtoi(A)