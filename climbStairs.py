class Solution(object):
	def climbStairs(self,n):
		if n<3:
			return n
		result = [0 for i in range(n)]
		result[0] = 1
		result[1] = 2
		for i in range(2,n):
			result[i] = result[i-1]+result[i-2]
		print result
		return result[n-1]

s = Solution()
print s.climbStairs(10)
