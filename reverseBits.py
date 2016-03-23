class Solution(object):
	def reverseBits(self,n):
		result = 0
		m = n
		i = 0
		while(i<32):
			#print m&1,
			result += m&1
			m >>=1
			result <<=1
			i+=1
		result >>=1
		return result

s = Solution()
print s.reverseBits(43261596)
