def anagrams(A):

    groups = dict()
    for i in range(len(A)):
        string = A[i]
        temp = "".join(sorted(string))
        if groups.get(temp, []) == []:
            groups[temp] = []
            groups[temp].append(i + 1)
        else:
            groups[temp].append(i + 1)
    return groups.values()


def anagramsII(B):
    groups = dict()
    strings = B.split()
    for i in range(len(strings)):
        string = strings[i]
        temp = "".join(sorted(string))
        if groups.get(temp, []) == []:
            groups[temp] = []
            groups[temp].append(i + 1)
        else:
            groups[temp].append(i + 1)
    return groups.values()


A = ["cat", "dog", "god", "tca"]
B = "cat dog god tca"


print anagrams(A)
print anagramsII(B)

