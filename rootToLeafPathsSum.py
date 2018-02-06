def sumPaths(A, B):
    if not A:
        return []
    res = []
    queue = [(A, A.val, [A.val])]
    while queue:
        curr, val, ls = queue.pop(0)
        if not curr.left and not curr.right and val == B:
            res.append(ls)
        if curr.left:
            queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
        if curr.right:
            queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
    return res