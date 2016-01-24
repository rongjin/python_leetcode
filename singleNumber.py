class Solution(object):
	def singleNumber(self,nums):
		result = 0
		for i in nums:
			result = result^i
		return result

nums = [1,2,3,2,1]
s = Solution()
print s.singleNumber(nums)
