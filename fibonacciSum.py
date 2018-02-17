def fibsum(N):
    fibs = [0]
    fib = 1
    while fib <= N:
        fibs.append(fib)
        fib = fibs[-1] + fibs[-2]

    count = 0
    for i in (len(fibs)-1,0,-1):
        num = fibs[i]
        if N >= num:
            N -= num
            count += 1
        if N == 0:
            break
    return fibs, count

N = 3

print fibsum(N)