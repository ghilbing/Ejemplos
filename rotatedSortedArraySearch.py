def search(A, B):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = start + (end - start) / 2
        if B == A[mid]:
            return mid
        if A[start] <= A[mid]:
            if A[start] <= B <= A[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if A[mid] <= B <= A[end]:
                start = mid + 1
            else:
                end = mid -1
    return -1


def searchII(self, nums, target):
    if not nums:
        return -1
    return self.binarySearch(nums, target, 0, len(nums) - 1)


def binarySearch(self, nums, target, start, end):
    if end < start:
        return -1
    mid = (start + end) / 2
    if nums[mid] == target:
        return mid
    if nums[start] <= target < nums[mid]:  # left side is sorted and has target
        return self.binarySearch(nums, target, start, mid - 1)
    elif nums[mid] < target <= nums[end]:  # right side is sorted and has target
        return self.binarySearch(nums, target, mid + 1, end)
    elif nums[mid] > nums[end]:  # right side is pivoted
        return self.binarySearch(nums, target, mid + 1, end)
    else:  # left side is pivoted
        return self.binarySearch(nums, target, start, mid - 1)



A = [ 180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177 ]
B = 42

print search(A, B)
print searchII(self, A, B)