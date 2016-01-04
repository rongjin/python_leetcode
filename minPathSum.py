class Solution(object):
	def minPathSum(self,grid):
		m = len(grid)
		if m==0:
			return 0
		n = len(grid[0])
		if n==0:
			return 0
		mat = [[0 for i in range(n)] for i in range(m)]
		mat[0][0] = grid[0][0]
		for i in range(m):
			for j in range(n):
				if i==0 and j == 0:
					continue
				elif i==0:
					mat[i][j]=mat[i][j-1]+grid[i][j]
				elif j==0:
					mat[i][j]=mat[i-1][j]+grid[i][j]
				else:
					mat[i][j] = min(mat[i-1][j],mat[i][j-1])+grid[i][j]
		return mat[m-1][n-1]


