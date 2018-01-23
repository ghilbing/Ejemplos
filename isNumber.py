def isNumber(A):
    A = A.strip()
    length = len(A)
    i = 0

    if i < length and (A[i] == "+" or A[i] == "-"):
        i += 1
    is_normal = 0
    is_exp = 1

    while i < length and A[i].isdigit():
        is_normal = 1
        i += 1

    if i < length and A[i] == '.':
        i += 1
        while i < length and A[i].isdigit():
            is_normal = 1
            i += 1
    if is_normal and i < length and (A[i] == 'e' or A[i] == 'E'):
        i += 1
        is_exp = 0
        if i < length and (A[i] == '+' or A[i] == '-'):
            i += 1
        while i < length and A[i].isdigit():
            i += 1
            is_exp = 1
    if is_normal == True:
        return 1
    else:
        return 0
    if is_exp == True:
        return 1
    else:
        return 0
    return i == length


def isNumber2(A):
    A = A.strip()
    n = len(A)
    if n == 0:
        return 0
    if A[0] == '+' or A[0] == '-':
        A = A[1:]
        n = n - 1
        if n == 0:
            return 0
        i = 0
        dotEncountered = False
        eEncountered = False
        while i < n:
            if A[i] >= '0' and A[i] <= '9':
                i += 1
                continue
            if A[i] == '.':
                if dotEncountered:
                    return 0
                dotEncountered = True
                i += 1
                if i >= n:
                    return 0
                elif A[i] == 'e':
                    return 0
            elif A[i] == 'e':
                if eEncountered:
                    return 0
                eEncountered = True
                dotEncountered = True
                i += 1
                if i < n and (A[i] == '-' or A[i] == '+'):
                    i += 1
            else:
                return 0
        return 1


print isNumber("3.e-23")
print isNumber(".2e81")
print isNumber("2e10")
print isNumber(" 0.1")
print isNumber("1 b")
print isNumber("3-3")
print isNumber("abc")
print isNumber("3e1.1")

print isNumber2("3.e-23")
print isNumber2(".2e81")
print isNumber2("2e10")
print isNumber2(" 0.1")
print isNumber2("1 b")
print isNumber2("3-3")
print isNumber2("abc")
