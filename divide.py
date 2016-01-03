class Solution(object):
	def __init__(self):
		self.MAX_INT = 0x7FFFFFFF
	def divide(self,dividend,divisor):
		result = 0
		pos = 1
		if(dividend<0):
			pos *= -1
			dividend *= -1
		if divisor<0:
			pos *= -1
			divisor *= -1
		while(dividend>=divisor):
			k = divisor
			t = 1
			while(k<=dividend):
				k = k<<1
				t = t<<1
			dividend-=k>>1
			result += t>>1
			#print dividend,result
		if pos == 1 and result > self.MAX_INT:
			return self.MAX_INT
		return result*(pos)
s = Solution()
print s.divide(1,-1)
