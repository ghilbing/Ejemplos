def countAndSay(A):
    seq = [1]

    for i in range(A - 1):
        next_seq = []
        num = seq[0]
        count = 0

        for j in range(len(seq)):
            if seq[j] == num:
                count += 1
            else:
                next_seq.extend([count, num])
                num, count = seq[j], 1

        next_seq.extend([count, num])

        seq = next_seq

    return "".join(str(x) for x in seq)

A = 7

print countAndSay(A)
