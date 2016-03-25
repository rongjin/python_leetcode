class Solution(object):
	def countPrimes(self,n):
		if n<3:
			return 0
		result = [1 for i in range(n)]
		result[0] = 0
		result[1] = 0
		for i in range(2,n):
			if result[i]==0:
				continue
			k = 2*i
			while(k<n):
				result[k]=0
				k+=i
		return sum(result)

s = Solution()
s.countPrimes(20)
