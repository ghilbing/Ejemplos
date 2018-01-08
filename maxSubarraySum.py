def maxSubarraySum(A):
    max_ending_here = max_so_far = A[0]
    for number in A[1:]:
        max_ending_here = max(max_ending_here + number, number)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


A = [-163, -20]

print maxSubarraySum(A)
