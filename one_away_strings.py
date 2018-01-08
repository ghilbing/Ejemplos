def is_one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    edits = 0
    i = 0
    j = 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edits == 1:
                return False
            if len(s1) > len(s2):
                i +=1
            elif len(s1) < len(s2):
                j +=1
            else:
                i +=1
                j +=1
                edits +=1
        else:
            i +=1
            j +=1
    if i < len(s1) or j < len(s2):
        edits +=1
    if edits == 1 or edits == 0:
        return True


s1 = ['a', 'b', 'c', 'd', 'e']
s2 = ['a', 'b', 'c', 'd', 'a', 'h', 'j']

print is_one_away(s1, s2)