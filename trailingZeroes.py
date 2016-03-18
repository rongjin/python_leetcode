class Solution(object):
	def trailingZeroes(self,n):
		result = 0
		m = 5
		while(n>0):
			result += n/m
			n = n/m
		return result

s = Solution()
print s.trailingZeroes(125)

