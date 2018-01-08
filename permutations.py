# from itertools import permutations
# perms = [''.join(i) for i in permutations(['s','t','a','c','k'])]
#
# print perms
# print len(perms)
# print len(set(perms))

def f(s):
    if len(s) == 2:
        X = [s, (s[1] + s[0])]
        return X
    else:
        list1 = []
        for i in range(0, len(s)):
            Y = f(s[0:i] + s[i+1: len(s)])
            for j in Y:
                list1.append(s[i] + j)
        return list1
s = "exam"
z = f(s)
print z
print len(z)


def perm(string):
    res = []
    for j in range(0, len(string)):
        if(len(string)>1):
            for i in perm(string[1:]):
                res.append(string[0]+i)
        else:
            return [string]
        string = string[1:]+string[0]
    return res


string = "exam"
print perm(string)








