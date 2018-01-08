def longestPalindromicSubstring(A):
    for l in substring(A):
        if palindrome(l):
            return l


def substring(A):
    length = len(A)

    for end in range(length, 0, -1):
        for i in range(length - end + 1):
            yield A[i: i + end]


def palindrome(A):
    return A == A[::-1]

def substringPalindrome(A):
    for n in range(len(A), 0, -1):
        searching = True
        i = 0
        s = ""
        # print('n:'+str(n))
        # checking out n size window from index i
        while searching:
            # print('i: '+str(i)+' end:'+str(i+n-1))
            if n == 1:
                return A[0]
            if i + n > len(A):
                # out of index array
                break
            else:
                s = A[i:i + n]
                r = s[::-1]
                if s == r:
                    searching == False
                    break
                # print('s:'+s+' r:'+r)
                s = ""
            i += 1
        if len(s) > 0:
            return s
    return None


    #interviewbit solution
def longestPalindrome(A):
    s = A
    if len(s) <= 1:
        return s
        low, high, st, size = 0, len(s) - 1, 0, 1
        for i in range(1, len(s)):
            low, high = i - 1, i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if size < high - low + 1:
                    st = low
                    size = high - low + 1
                low -= 1
                high += 1
                pass
            low, high = i - 1, i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if size < high - low + 1:
                    st = low
                    size = high - low + 1
                low -= 1
                high += 1
                pass
            pass
        # print st,size
        return s[st:st + size]


A = "aaaacbcaaaa"

print longestPalindromicSubstring(A)
print substringPalindrome(A)
print longestPalindrome(A)
