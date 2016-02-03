class Solution(object):
	def check(self,row):
		print row
		mydict = {}
		for i in row:
			if i!=".":
				if i not in "123456789":
					return False
				if i in mydict:
					return False
				else:
					mydict[i]=1
		return True

	def checkrow(self,board):
		for row in board:
			if not self.check(row):
				return False
		return True
	def checkcol(self,board):
		for i in range(len(board)):
			row = []
			for j in range(len(board)):
				row.append(board[j][i])
			if not self.check(row):
				return False
		return True
	def checkgrid(self,board):
		for i in range(9):
			row = []
			loci = i/3
			locj = i%3
			for ii in range(3):
				for jj in range(3):
					row.append(board[loci*3+ii][locj*3+jj])
			if not self.check(row):
				return False
		return True
	def isValidSudoku(self,board):
		r1 = self.checkrow(board)
		if not r1:
			return False
		r2 = self.checkcol(board)
		if not r2:
			return False
		r3 = self.checkgrid(board)
		if not r3:
			return False
		return True
		
s = Solution()
board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
board = [".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]
for i in board:
	print i
print
print s.isValidSudoku(board)
