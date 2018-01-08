from collections import Counter
import itertools


def degreeArray(A):
        left, right, count = {}, {}, {}
        array = []
        for j in range(1, len(A)):
            array.append(A[j])
        for i, x in enumerate(array):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(A)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans


A = [5, 1, 2, 2, 3, 1, 2]

print degreeArray(A)
