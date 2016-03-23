class Solution(object):
	def help(self,grid,i,j,row,col,mymax):
		if grid[i][j]==1:
			grid[i][j] = mymax
			if i>=1 and grid[i-1][j]<2:
				self.help(grid,i-1,j,row,col,mymax)
			if j>=1 and grid[i][j-1]<2:
				self.help(grid,i,j-1,row,col,mymax)
			if i<row-1 and grid[i+1][j]<2:
				self.help(grid,i+1,j,row,col,mymax)
			if j<col-1 and grid[i][j+1]<2:
				self.help(grid,i,j+1,row,col,mymax)

	def numIslands(self,grid):
		row = len(grid)
		if row==0:
			return 0
		col = len(grid[0])
		mymax = 1
		for i in range(row):
			for j in range(col):
				if grid[i][j]==1:
					mymax += 1
					self.help(grid,i,j,row,col,mymax)
		return mymax-1

s = Solution()
grid = [[1,0],[1,1]]
print s.numIslands(grid)
