class Solution(object):
	def help(self,board,i,j):
		if board[i][j]!='O':
			return
		board[i][j]='.'
		if i-1>0:
			self.help(board,i-1,j)
		if i+1<len(board)-1:
			self.help(board,i+1,j)
		if j-1>0:
			self.help(board,i,j-1)
		if j+1<len(board[0])-1:
			self.help(board,i,j+1)

	def solve(self,board):
		h = len(board)
		if h==0:
			return
		w = len(board[0])
		for i in range(w):
			if board[0][i]=='O':
				self.help(board,0,i)
			if board[h-1][i]=='O':
				self.help(board,h-1,i)
		for i in range(h):
			if board[i][0]=='O':
				self.help(board,i,0)
			if board[i][w-1]=='O':
				self.help(board,i,w-1)
		for i in range(h):
			for j in range(w):
				if board[i][j]=='O':
					board[i][j]='X'
				elif board[i][j]=='.':
					board[i][j]='O'

s = Solution()
board = ['O']
s.solve(board)
for i in board:
	print i
