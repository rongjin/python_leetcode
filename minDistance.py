class Solution(object):
	def setmat(self,i,j,word1,word2,mat):
		if j==0:
			mat[i][j] = mat[i-1][j]+1
		else:
			mylist = []
			if word1[j-1] == word2[i-1]:
				mylist.append(mat[i-1][j-1])
			else:
				mylist.append(mat[i-1][j-1]+1)#replace
			mylist.append(mat[i-1][j]+1)#insert in word1
			mylist.append(mat[i][j-1]+1)#delete in word1
			mat[i][j] = min(mylist)
		return mat[i][j]

	def minDistance(self,word1,word2):
		m = len(word2)
		n = len(word1)
		if n == 0:
			return m
		if m == 0:
			return n
		mat = [[10000 for i in range(n+1)] for i in range(m+1)]
		for i in range(n+1):
			mat[0][i] = i
		for i in range(1,m+1):
			for j in range(n+1):
				self.setmat(i,j,word1,word2,mat)
		for i in mat:
			print i
		return mat[m][n]

s = Solution()
word1 = "park"
word2 = "spake"
s.minDistance(word1,word2)
