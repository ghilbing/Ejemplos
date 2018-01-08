def primeNumber(num):
    for j in range(len(num)):

        for i in range(2, int(num[j] ** 0.5) + 1):
            if num[j] % i == 0:
                print False
                print num[j]

        print True
        print num[j]




num = [5, 3, 4, 7, 9, 15, 32, 19, 44, 33]

print primeNumber(num)
