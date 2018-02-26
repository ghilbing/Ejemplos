def minJump(A):
    last_max_reach = 0
    current_max_reach = 0
    njump = 0
    i = 0
    while current_max_reach < len(A)-1:
        while i <= last_max_reach:
            current_max_reach = max(i+A[i], current_max_reach)
            i += 1
        if last_max_reach == current_max_reach:
            return -1
        last_max_reach = current_max_reach
        njump += 1
    return njump


A = [2,3,1,1,4]

print minJump(A)