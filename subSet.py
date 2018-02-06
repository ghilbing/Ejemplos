def subSet(A):
    subs = [[]]
    for item in sorted(A):
        subs += [prev_subs + [item] for prev_subs in subs]
    return sorted(subs)


A = [1, 2, 3, 4]

print subSet(A)