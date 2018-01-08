def shortestPalindrome(A):
    reversed = A[::-1]
    i = 0
    count = 0

    while i < len(A):
        if A[0:len(A) - i] == reversed[i:]:
            break
        i += 1

    A = reversed[0:i] + A

    count = len(reversed[0:i])



    return count

A = ['a', 'a', 'a', 'a', 'a']
print shortestPalindrome(A)