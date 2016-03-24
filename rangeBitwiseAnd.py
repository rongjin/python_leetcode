class Solution(object):
	def rangeBitwiseAnd(self,m,n):
		if m==0:
			return 0
		k = m^n
		d = 0
		while(k>0):
			k>>=1
			d+=1
		k = 1
		result = m
		while(d>0):
			result &= ~k
			k<<=1
			d-=1
		return result

s = Solution()
print s.rangeBitwiseAnd(11,12)
print s.rangeBitwiseAnd(5,7)
print s.rangeBitwiseAnd(0,2147483647)
