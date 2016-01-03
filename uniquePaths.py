class Solution(object):
	def uniquePaths(self,m,n):
		mat = [[0 for i in range(n)] for i in range(m)]
		mat[0][0] = 1
		for i in range(m):
			for j in range(n):
				if i == 0 or j==0:
					mat[i][j]=1
				else:
					mat[i][j] = mat[i-1][j]+mat[i][j-1]

		for i in mat:
			print i
		return mat[m-1][n-1]

s = Solution()
print s.uniquePaths(3,7)
