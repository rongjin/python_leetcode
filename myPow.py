class Solution(object):
	def myPow(self,x,n):
		m = abs(n)
		result = 1.0
		while(m):
			if m & 1:
				result *= x
			m = m>>1
			x = x*x
		if n>=0:
			return result
		else:
			return 1/result

s = Solution()
print s.myPow(1.5,-2)
