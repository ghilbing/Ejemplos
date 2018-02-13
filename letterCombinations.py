def letterCombinations(A):
    keyboard = {'0':'0', '1':'1', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    allCombinations = [''] if A else []
    for n in A:
        combinations = list()
        for letter in keyboard[n]:
            for combination in allCombinations:
                combinations.append(combination + letter)
        allCombinations = combinations
    return sorted(allCombinations)

A = "23"

print letterCombinations(A)