def is_permutation(a, b):
    if len(a) != len(b):
        return False
    ascii = [0] * 256
    for c in a:
        ascii[ord(c)] +=1

    for c in b:
        ascii[ord(c)] -=1
        if ascii[ord(c)] <0:
            return False
    return True


print is_permutation("hola", "ohle")
