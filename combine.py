class Solution(object):
	def combine(self,n,k):
		result = self.help(n,k,1)
		return result

	def help(self,n,k,i):
		if k == 1:
			mylist = []
			for i in range(i,n+1):
				mylist.insert(0,[i])
			return mylist
		else:
			mylist = []
			for ii in range(i,n+1):
				print ii
				if k-2<=n-ii-1:
					result = self.help(n,k-1,ii+1)
					for j in result:
						j.insert(0,ii)
						mylist.insert(0,j)
			return mylist
s = Solution()
result = s.combine(3,3)
for i in result:
	print i
