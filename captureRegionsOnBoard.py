def solve(board):
    if not board:
        return
    m = len(board)
    n = len(board[0])

    save = [ij for k in range(m + n) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
    while save:
        i, j = save.pop()
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = 'S'
            save += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
            # board[:] = [['XO'[c == 'S'] for c in row] for row in board]
    for row in board:
        for i, c in enumerate(row):
            row[i] = 'XO'[c == 'S']

    return board


board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]

print solve(board)

from collections import defaultdict


def init(A):
    n = len(A)
    m = len(A[0])
    x = defaultdict(list)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'O':
                x[(i, j)].append([i, j])
            if i + 1 < n:
                if A[i][j] == 'O' and A[i + 1][j] == 'O':
                    x[(i, j)].append([i + 1, j])
            if j + 1 < m:
                if A[i][j] == 'O' and A[i][j + 1] == 'O':
                    x[(i, j)].append([i, j + 1])
            if i - 1 >= 0:
                if A[i][j] == 'O' and A[i - 1][j] == 'O':
                    x[(i, j)].append([i - 1, j])
            if j - 1 >= 0:
                if A[i][j] == 'O' and A[i][j - 1] == 'O':
                    x[(i, j)].append([i, j - 1])
    # print(x)
    return x


def dfs(v, graph, visited, m, n, ans):
    st = []
    st.append(v)
    s = True
    while len(st) > 0:
        x = st.pop()
        ans.append(x)
        if x[0] == 0 or x[0] == n - 1 or x[1] == 0 or x[1] == m - 1:
            s = False
        for i in graph[tuple(x)]:
            if visited[i[0]][i[1]] == False:
                visited[i[0]][i[1]] = True
                st.append(i)

    return s


def change(graph, n, m, A):
    visited = [[False for i in range(m)] for j in range(n)]
    # print(visited)
    count = 0
    for i in graph:
        ans = []
        if visited[i[0]][i[1]] == False:
            visited[i[0]][i[1]] = True
            s = dfs(i, graph, visited, m, n, ans)
            # print(ans,s)
            if s:
                for i in ans:
                    A[i[0]][i[1]] = 'X'


class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        graph = init(A)
        # print(graph)
        n = len(A)
        m = len(A[0])
        change(graph, n, m, A)


class Solution:
    # @param A : list of list of chars


    def uncapturedDFS(self, A, row, col):
        # Perform DFS on edge O and mark all connected O's as +
        A[row][col] = '+'
        # Look up (if not top row)
        if row > 0 and A[row - 1][col] == 'O':
            A = self.uncapturedDFS(A, row - 1, col)
        # Look down (if not bottom row)
        if row < len(A) - 1 and A[row + 1][col] == 'O':
            A = self.uncapturedDFS(A, row + 1, col)
        # Look left (if not left column)
        if col > 0 and A[row][col - 1] == 'O':
            A = self.uncapturedDFS(A, row, col - 1)
        # Look right (if not right column)
        if col < len(A[0]) - 1 and A[row][col + 1] == 'O':
            A = self.uncapturedDFS(A, row, col + 1)
        return A

    def flagRim(self, A):
        # Identify Os on the top and bottom borders of the matrix
        for top_col, top in enumerate(A[0]):
            if top == 'O':
                A = self.uncapturedDFS(A, 0, top_col)
        for bottom_col, bottom in enumerate(A[-1]):
            if bottom == 'O':
                A = self.uncapturedDFS(A, len(A) - 1, bottom_col)
        # Flag O's on the left and right hand borders
        for left_row in xrange(len(A)):
            if A[left_row][0] == 'O':
                A = self.uncapturedDFS(A, left_row, 0)
        for right_row in xrange(len(A)):
            if A[right_row][-1] == 'O':
                A = self.uncapturedDFS(A, right_row, len(A[0]) - 1)
        return A

    def convert(self, A):
        for i, row in enumerate(A):
            for j, value in enumerate(row):
                if value == '+':
                    A[i][j] = 'O'
                if value == 'O':
                    A[i][j] = 'X'
        return A

    def solve(self, A):
        # Find regions of O's that are not enclosed
        A = self.flagRim(A)
        # Format output to indicate whether region is enclosed
        A = self.convert(A)
        return A
