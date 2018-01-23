def ifPowerOfTwo(A):
    return (A > 0) and (A & (A-1))==0

def powerOfTwo(A):
    return A > 0 and bin(A).count('1') == 1

def power(A):
   x = int(A)
   if x>=2 and (x & (x-1))==0:
       return 1
   else:
       return 0


A = 2

print ifPowerOfTwo(A)
print powerOfTwo(A)
print power(A)