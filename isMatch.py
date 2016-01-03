class Solution(object):
	def help(self,i,j,s,p,mat):
		if j == 0:
			if mat[i-1][j]==1 and p[i-1] == '*':
				return 1
			else:
				return 0
		else:
			chars = s[j-1]
			charp = p[i-1]
			if charp == '?':
				if mat[i-1][j-1]==1:
					return 1
				else:
					return 0
			elif charp == '*':
				if mat[i][j-1]==1 or mat[i-1][j]==1 or mat[i-1][j-1]==1:
					return 1
				else:
					return 0
			else:
				if mat[i-1][j-1]==1 and chars==charp:
					return 1
				else:
					return 0
		return 0
	def isMatch(self,s,p):
		l1 = len(s)
		l2 = len(p)
		if l2-p.count('*')>l1:
			return False
		mat = [[0 for x in range(l1+2)] for x in range(l2+1)]
		mat[0][0] =1
		for i in range(1,l2+1):
			for j in range(l1+1):
				mat[i][j] = self.help(i,j,s,p,mat)
                    #for k in mat:
                    #print k
                    #print
		return mat[l2][l1]

sl = Solution()
s="a"
p="a"
print sl.isMatch(s,p)
