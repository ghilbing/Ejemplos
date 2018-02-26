

def countUnique(left, right):
    count = 0
    for i in range(left, right):
        num = i
        visited = [False] * 10
        while num:
            if visited[num % 10]:
                 break
            visited[num % 10] = True
            num = num / 10
        if num == 0:
            count += 1
            continue
    return count + 1

def countNumbers(arr):
    rows = len(arr)
    cols = len(arr[0])
    res = []

    for i in range(1,rows):
            start = arr[0][i]
            end = arr[i][-1]
            res.append(countUnique(start, end))
    return res

arr = [[1,20], [52, 80], [57,64]]

print countNumbers(arr)