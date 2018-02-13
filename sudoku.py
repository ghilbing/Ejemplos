import copy

A = [
    ".........",
    "5.3.67...",
    "9..3421..",
    ".....4...",
    "..1...72.",
    "..2.1....",
    ".3......9",
    ".8.1..2..",
    "...75.8.6"
]
from aetypes import end


# board = [
#    ".........",
#    ".........",
#     ".........",
#     ".........",
#     ".........",
#     ".........",
#     ".........",
#     ".........",
#     "........."
# ]


# board = [
# "6..874.1.",
# "..9.36...",
# "...19.8..",
# "7946.....",
# "..1.894..",
# "...41..69",
# ".7..5..9.",
# ".539.76..",
# "9.2.61.47"
# ]

def solveSudoku(A):
    def isValid(x, y):
        temp = A[x][y]
        A[x][y] = 'D'
        for i in range(9):
            if A[i][y] == temp:
                return False
        for i in range(9):
            if A[x][i] == temp:
                return False
        for i in range(3):
            for j in range(3):
                if A[(x / 3) * 3 + i][(y / 3) * 3 + j] == temp:
                    return False
        A[x][y] = temp
        return True

    def dfs(A):
        for i in range(9):
            for j in range(9):
                if A[i][j] == '.':
                    for k in '123456789':
                        A[i][j] = k
                        if isValid(i, j) and dfs(A):
                            return True
                        A[i][j] = '.'
                    return False
        return True

    dfs(A)

print solveSudoku(A)