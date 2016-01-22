class Solution(object):
	def help(self,s,mat):
		l = len(s)
		for i in range(l):
			mat[i][i]=1
			l = i-1
			r = i+1
			while(l>=0 and r<len(s) and s[l]==s[r]):
				mat[l][r]=1
				l -= 1
				r += 1
			l = i
			r = i+1
			while(l>=0 and r<len(s) and s[l]==s[r]):
				mat[l][r]=1
				l -=1
				r +=1
	def minCut(self, s):
		l = len(s)
		mat = [[0 for i in range(l)] for i in range(l)]
		self.help(s,mat)
		mylist = [0 for i in range(l)]
		for i in range(1,l):
			if mat[0][i]==1:
				mylist[i]=0
			else:
				mymin = i
				for j in range(i):
					if mat[j+1][i]==1:
						value = mylist[j]+1
						if value<mymin:
							mymin = value
				mylist[i] = mymin
		print mylist
		return mylist[-1]


s = Solution()
mystring = "abccd"
print s.minCut(mystring)

