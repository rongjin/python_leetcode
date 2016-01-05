class Solution(object):
	def setZeroes(self,matrix):
		m = len(matrix)
		n = len(matrix[0])
		row0 = 1
		col0 = 1
		for i in range(0,m):
			for j in range(0,n):
				if matrix[i][j]==0:
					matrix[i][0] = 0
					matrix[0][j] = 0
					if i==0:
						row0 = 0
					if j==0:
						col0 = 0
		for i in range(1,m):
			if matrix[i][0]==0:
				for j in range(0,n):
					matrix[i][j] = 0
		for j in range(1,n):
			if matrix[0][j]==0:
				for i in range(0,m):
					matrix[i][j] = 0
		if row0==0:
			for i in range(1,n):
				matrix[0][i]=0
		if col0==0:
			for j in range(0,m):
				matrix[j][0]=0
		print
		for i in matrix:
			print i
s = Solution()
mat = [[1 for i in range(7)] for i in range(3)]
mat[1][1] = 0
mat[2][6] = 0
mat = [[1,0],[1,1]]

s.setZeroes(mat)
