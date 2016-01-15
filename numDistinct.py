class Solution(object):
	def help(self,s,t,i,j,mat):
		if s[i-1]==t[j-1]:
			mat[i][j]+=mat[i-1][j-1]
		mat[i][j]+=mat[i-1][j]

	def numDistinct(self,s,t):
		ls = len(s)+1
		lt = len(t)+1
		print ls,lt
		mat = [[0 for i in range(lt)] for i in range(ls)]
		for i in range(ls):
			mat[i][0] = 1
		for i in range(1,ls):
			for j in range(1,lt):
				self.help(s,t,i,j,mat)
		return mat[ls-1][lt-1]

s = Solution()
mys = "rabbbiit"
myt = "rabbit"
print s.numDistinct(mys,myt)
