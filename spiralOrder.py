def printSpiral(matrix):
   if not matrix or not matrix[0]:
       return []
   ans = []
   m = len(matrix)
   n = len(matrix[0])
   u = 0
   d = m -1
   l = 0
   r = n -1

   while l < r and u < d:
       ans.extend([matrix[u][j] for j in range(l,r)])
       ans.extend([matrix[i][r] for i in range(u,d)])
       ans.extend([matrix[d][j] for j in range(r,l, -1)])
       ans.extend([matrix[i][l] for i in range(d,u, -1)])
       u +=1
       d -=1
       l +=1
       r -=1
   if l == r:
        ans.extend([matrix[i][r] for i in range(u,d + 1)])
   elif u == d:
        ans.extend([matrix[u][j] for j in range(l, r + 1)])
   return ans


matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

print printSpiral(matrix)