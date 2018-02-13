def singleNumber(A):
    first = 0
    second = 0
    for n in A:
        # Set the bits to first, if the bits were already set,
        # they are going to get toggled, then we check if they aren't
        # in the second variable by doign a negation of the variable and
        # an and
        first = (first ^ n) & ~second
        # We do another xor in case the first one toggled the bits, and
        # After that we need to check that we don't have any bits set in
        # the first bitset.
        second = (second ^ n) & ~first
    return first

A = [2,2,2,3,3,3,4,4,4,5]

print singleNumber(A)