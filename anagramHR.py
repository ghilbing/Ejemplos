def anabgran(A):
    length = A[0]
    cant = [0 * 26]
    wordNum = ord('a')
    res = 0
    size = len(str(A[1]))
    for w in range(1,length):
        if len(str(w)) % 2 != 0:
            return -1
        else:
            for i in range(0, len(str(w)) / 2):
                cant[ord(i) - wordNum] += 1
            for j in range(len(str(w)) / 2, len(str(w))):
                cant[ord(j) - wordNum] -= 1
    for num in cant:
        res += abs(num)
    return length





A= [10,
"hhpddlnnsjfoyxpciioigvjqzfbpllssuj",
"xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj",
"dnqaurlplofnrtmh",
"aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb",
"lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad",
"drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe",
"ubulzt",
"vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy",
"xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa",
"gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv"]


print anabgran(A)