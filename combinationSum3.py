class Solution(object):
	def __init__(self):
		self.result = []
	def help(self,k,n,l,r,cur):
		print k,n,l,r,cur
		if k==1:
			if n>= l and n<=r:
				cur.append(n)
				ss = []
				for i in cur:
					ss.append(i)
				self.result.append(ss)
				cur.pop()
		else:
			for i in range(l,min(n,r+1)):
				cur.append(i)
				self.help(k-1,n-i,i+1,r,cur)
				cur.pop()

	def combinationSum3(self,k,n):
		self.help(k,n,1,9,[])
		return self.result

s= Solution()
print s.combinationSum3(3,9)

