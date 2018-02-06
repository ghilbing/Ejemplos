def numSetBits(A):
    return str(bin(A)).count('1')

A= "00000000000000000000000000001011"

#print numSetBits(A)

def numSetBitsII(A):
    count = 0
    while A>0:
        A &= A - 1
        count +=1
    return count

print numSetBitsII(A)