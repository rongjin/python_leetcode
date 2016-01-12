class Solution(object):
	def __init__(self):
		self.record = []
	def numTrees(self,n):
		if n==0:
			return 1
		elif n==1:
			return 1
		if self.record == []:
			self.record = [-1 for i in range(n+1)]
		result = 0
		for i in range(1,n+1):
			d = 1
			if self.record[i-1]!=-1:
				d*= self.record[i-1]
			else:
				f = self.numTrees(i-1)
				self.record[i-1] = f
				d*=f
			if self.record[n-i]!=-1:
				d*= self.record[n-i]
			else:
				f = self.numTrees(n-i)
				self.record[n-i]= f
				d*=f
			result +=d
		self.record[n] = result
		return result

s = Solution()
print s.numTrees(19)
