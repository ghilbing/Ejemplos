#This is working
def partitionWorking(A):
    ans = []
    length = len(A)

    def partitionHelper(arr, index):
        if index == length:
            ans.append(arr)
        else:
            for i in range(index, length):
                if A[index:i + 1] == A[index:i + 1][::-1]:
                    partitionHelper(arr + [A[index:i + 1]], i + 1)


    partitionHelper([], 0)

    return ans
A = ["a", "a", "b"]
s = ["e", "f", "e"]

print partitionWorking(s)




def partition(s):
    return [[s[:i]] + rest
            for i in xrange(1, len(s) + 1)
            if s[:i] == s[i - 1::-1]
            for rest in partition(s[i:])] or [[]]

s = ["e", "f", "e"]
A = ["a", "a", "b"]

print partition(s)


def partitionII(A):
    res = []
    dfs(A, [], res)
    return res

def dfs(A, path, res):
    if not A:
        res.append(path)
    for i in range(1, len(A)+1):
        if isPal(A[:i]):
            dfs(A[i:], path+[A[:i]], res)

def isPal(A):
    return A == A[::-1]

#print partitionII(A)


def partitionIII(A):
    return helper(s, {})


def helper(A, h):
    if A in h:
        return h[A]
    h[A] = []
    for i in range(len(A)):
        if A[:i + 1] == A[:i + 1][::-1]:
            if i + 1 == len(s):
                h[A].append([A])
            else:
                for rest in helper(A[i + 1:], h):
                    h[A].append([A[:i + 1]] + rest)
    return h[A]

#print partitionIII(A)