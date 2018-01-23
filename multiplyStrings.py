def multiplyStrings(A,B):
    product = [0] * (len(A) + len(B))
    position = len(product)-1

    for nro1 in reversed(A):
        tempPos = position
        for nro2 in reversed(B):
            product[tempPos] += int(nro1) * int(nro2)
            product[tempPos-1] += product[tempPos]/10
            product[tempPos] %= 10
            tempPos -=1
        position -=1

    pt = 0
    while pt < len(product)-1 and product[pt] ==0:
        pt +=1

    return ''.join(map(str, product[pt:]))

A = "12"
B = "10"

def multiply(A,B):
    res = 0
    carry1 = 1
    for n1 in reversed(A):
        carry2 = 1
        for n2 in reversed(B):
            res += int(n1) * int(n2) * carry1 * carry2
            carry2 *=10
        carry1 *=10

    return str(res)

print multiplyStrings(A, B)
print multiply(A,B)