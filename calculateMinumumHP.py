import sys
class Solution(object):
	def calculateMinimumHP(self,dungeon):
		row = len(dungeon)
		col = len(dungeon[0])
		mat = [[sys.maxint for i in range(col+1)] for j in range(row+1)]
		mat[row][col-1] = 1
		mat[row-1][col] = 1
		for i in range(row-1,-1,-1):
			for j in range(col-1,-1,-1):
				print i,j
				mat[i][j] = min(mat[i][j+1],mat[i+1][j])-dungeon[i][j]
				if mat[i][j]<1:
					mat[i][j] = 1
		for i in range(row+1):
			for j in range(col+1):
				print mat[i][j]," ",
			print
		print
		return mat[0][0]

s = Solution()
dung = [[0,0]]
print s.calculateMinimumHP(dung)

