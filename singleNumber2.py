class Solution(object):
	def singleNumber(self,nums):
		result = [0 for i in range(32)]
		for i in nums:
			for j in range(32):
				result[j] += i&1
				i = i>>1
				if i==0:
					break
		print result
		extra = 0
		for i in range(32):
			if i==31 and result[i]%3!=0:
				extra = -((1<<31)-extra)
			else:
				extra |= (result[i]%3)*(1<<i)
		return extra


s = Solution()
nums = [-1,-1,-1,-2,-2,-2,-3]
print nums
print s.singleNumber(nums)
