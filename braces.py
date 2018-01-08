def braces(A):
    braces1 = 0
    braces2 = 0
    braces3 = 0
    balanced = True

    n = A[0]

    for j in range(1, len(A)):
        strings = list(A[j])
        for i in range(0, len(strings)):
            if strings[i] == "{":
                braces1 = braces1 + 1
            elif strings[i] == "[":
                braces2 = braces2 + 1
            elif strings[i] == "(":
                braces3 = braces3 + 1
            elif strings[i] == "}":
                if braces1 == 0:
                    balanced = False
                else:
                    braces1 = braces1 - 1
            elif strings[i] == "]":
                if braces2 == 0:
                    balanced = False
                else:
                    braces2 = braces2 - 1
            elif strings[i] == ")":
                if braces3 == 0:
                    balanced = False
                else:
                    braces3 = braces3 - 1
        if braces1 == 0 and braces2 == 0 and braces3 == 0 and balanced == True:
            print "YES"
        else:
            print "NO"


A = [2, '{}[]()', '{[}]}']

print braces(A)
