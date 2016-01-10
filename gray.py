class Solution(object):
	def grayCode(self,n):
		l = 1<<n
		mylist = [0 for i in range(l)]
		for i in range(l):
			mylist[i] = i^(i>>1)
		return mylist

s = Solution()
print s.grayCode(2)

