def calculatingNChooseK(N, K):
    memo = {}

    if K == 0 or K == N:
        return 1

    def factorial(X):
        if X in memo:
            return memo[X]
        elif X == 0:
            return 1
        else:
            x = factorial(X - 1) * X
            memo[X] = x

        return x

    return factorial(N) / (factorial(K) * factorial(N - K))


N = 10
K = 4


def nck_recursive(N, K):
    if K == 0 or K == N:
        return 1
    else:
        return nck_recursive(N - 1, K) + nck_recursive(N - 1, K - 1)


def fact(N):
    if N <= 1:
        return 1
    else:
        return N * fact(N - 1)


def nck_factorial(N, K):
    return fact(N) / fact(K) * fact(N - K)


def nck_multiplicative(N, K):
    result = 1
    for i in range(1, K + 1):
        result = result * (N(K - i)) / i
    return result


print calculatingNChooseK(N, K)
print nck_recursive(N, K)
