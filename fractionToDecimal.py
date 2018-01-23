def fractionToDecimal(A,B):
    sign = '-' if A * B < 0 else ''
    numerator = abs(A)
    denominator = abs(B)
    decimal = ''
    decimal += str(numerator / denominator)
    numerator = numerator % denominator
    if numerator != 0:
        decimal += '.'
    fraction = ''
    i = 0
    seen = {}
    while numerator not in seen and numerator != 0:
        seen[numerator] = i
        i += 1
        numerator *= 10
        fraction += str(numerator / denominator)
        numerator = numerator % denominator

    if numerator != 0:
        fraction = fraction[:seen[numerator]] + '(' + fraction[seen[numerator]:] + ')'

    return sign + decimal + fraction

A = -1
B = 28

print fractionToDecimal(A, B)