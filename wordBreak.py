def wordBreak(A, B):
    wordLenList = set(map(len, B))
    sentences = [False for i in range(len(A))]
    for startIndex in range(len(A), -1, -1):
        for wordLen in wordLenList:
            if startIndex + wordLen > len(A) or A[startIndex: startIndex + wordLen] not in B:
                print A[startIndex: startIndex + wordLen]
                continue
            if startIndex + wordLen == len(A):
                sentences[startIndex] = True
                break
            else:
                if sentences[startIndex + wordLen]:
                    sentences[startIndex] = True
                    break
    if sentences[0]:
        return 1
    else:
        return 0
#A = "leetcodes"
#B = ["leet", "codes"]

A = "abababababaaaabaabbbabbbabbababbb"
B = [ "abbbabaa", "baabaaaab", "babaaaaaba", "b", "b", "bbaaaab", "aaabbb", "aabbbbbab", "abbb", "abaa", "aaababaab", "aabbabaa", "bab", "bbbbaabbb" ]


print wordBreak(A, B)