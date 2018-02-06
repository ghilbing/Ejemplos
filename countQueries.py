def counts(nums):
    lennums = nums[0]
    lenmaxes = lennums + 2
    queue = []
    A = []
    B = []
    res = []
    count = 0
    for i in range(1, lennums+1):
        A.append(nums[i])
    for j in range(lenmaxes, len(nums)):
        queue.append(nums[j])


    while queue:
        value = queue.pop()
        for i in range(0, len(A)):
            if A[i] > value:
                count += 1
        res.append(count)
        queue.pop()
    return res





    return res





nums = [4, 1, 4, 2, 4, 2, 3, 5]


print counts(nums)