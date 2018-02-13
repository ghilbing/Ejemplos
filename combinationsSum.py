def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res


def dfs(nums, target, index, path, res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        dfs(nums, target - nums[i], i, path + [nums[i]], res)


candidates = [3, 5, 7]
target = 28

print combinationSum(candidates, target)


def combinationSumII(A, B):
    result = []
    candidates = sorted(A)

    def dfsII(remain, stack):
        if remain == 0:
            result.append(stack)
            return

        for item in candidates:
            if item > remain: break
            if stack and item < stack[-1]:
                continue
            else:
                dfsII(remain - item, stack + [item])

    dfsII(B, [])
    return result

A = [8, 10, 6, 11, 1, 16, 8]
B = 28

print combinationSum(A, B)