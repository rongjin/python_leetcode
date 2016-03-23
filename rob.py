class Solution(object):
	def rob(self,nums):
		if len(nums)==0:
			return 0
		elif len(nums)==1:
			return nums[0]
		elif len(nums)==2:
			return max(nums[0],nums[1])
		elif len(nums)==3:
			return max(nums[0]+nums[2],nums[1])
		result = [nums[0],nums[1],nums[0]+nums[2]]
		for i in range(3,len(nums)):
			result.append(max(result[(i-3):(i-1)])+nums[i])
		return max(result[len(nums)-1],result[len(nums)-2])

s = Solution()
print s.rob([2,1,1,2])
