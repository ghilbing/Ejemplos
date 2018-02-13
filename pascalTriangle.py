def pascalTriangle(k):
    row = [1]
    s = [0]
    for i in range(max(k,0)):
        print ' '.join(str(e) for e in(row))
        row = [length+j for length, j in zip(row+s, s+row)]
    return k>=1

k = 4

pascalTriangle(k)