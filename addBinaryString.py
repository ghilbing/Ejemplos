def binAdding(A, B):
    result = ""
    carry = 0
    val = 0
    for i in xrange(max(len(A), len(B))):
        val = carry
        if i < len(A):
            val += int(A[-(i + 1)])
        if i < len(B):
            val += int(B[-(i + 1)])
        carry = val / 2
        val = val % 2
        result += str(val)
    if carry:
        result += str(carry)
    return result[::-1]


A = "111"
B = "111"

def addBinary(A,B):
    numA = int(A, 2)
    numB = int(B, 2)
    return bin(numA + numB)
    # return bin(int(A, 2) + int(B, 2))[2:]

print binAdding(A, B)
print addBinary(A, B)