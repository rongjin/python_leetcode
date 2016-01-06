class Solution(object):
	def help(self,board,word,i,j):
		print i,j
		if len(word)==0:
			return True
		else:
			if i>=1:
				if board[i-1][j]==word[0]:
					board[i-1][j]='0'
					if self.help(board,word[1:],i-1,j):
						return True
					board[i-1][j]=word[0]
			if j>=1:
				if board[i][j-1]==word[0]:
					board[i][j-1]='0'
					if self.help(board,word[1:],i,j-1):
						return True
					board[i][j-1]=word[0]
			if i+1<len(board):
				if board[i+1][j]==word[0]:
					board[i+1][j]='0'
					if self.help(board,word[1:],i+1,j):
						return True
					board[i+1][j]=word[0]
			if j+1<len(board[0]):
				if board[i][j+1]==word[0]:
					board[i][j+1]='0'
					if self.help(board,word[1:],i,j+1):
						return True
					board[i][j+1]=word[0]
	def exist(self,board,word):
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j]==word[0]:
					board[i][j]='0'
					if self.help(board,word[1:],i,j):
						return True
					board[i][j]=word[0]
		return False

s = Solution()
board = [['A','B','C','E'],
		['S','F','C','S'],
		['A','D','E','E']]
word = "ABCCED"
print s.exist(board,word)
