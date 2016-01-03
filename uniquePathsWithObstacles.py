class Solution(object):
	def uniquePathsWithObstacles(self,obstacleGrid):
		m = len(obstacleGrid)
		if m == 0:
			return 0
		n = len(obstacleGrid[0])
		if n == 0:
			return 0
		if obstacleGrid[0][0] == 1:
			return 0
		mat = [[0 for i in range(n)] for i in range(m)]
		mat[0][0]=1
		for i in range(m):
			for j in range(n):
				if obstacleGrid[i][j] == 1:
					mat[i][j] = 0
				elif i==0 and j==0:
					continue
				elif i==0:
					mat[i][j] = mat[i][j-1]
				elif j==0:
					mat[i][j] = mat[i-1][j]
				else:
					mat[i][j] = mat[i-1][j]+mat[i][j-1]
		for i in mat:
			print i
		print
		return mat[m-1][n-1]

s = Solution()
n = 2
m = 1
obs = [[0 for i in range(n)] for i in range(m)]
s.uniquePathsWithObstacles(obs)
