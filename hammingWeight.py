class Solution(object):
	def hammingWeight(self,n):
		result = 0
		while(n):
			result += n&1
			n>>=1
		return result

s = Solution()
print s.hammingWeight(11)
