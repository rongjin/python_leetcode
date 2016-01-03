class Solution(object):
	def help(self,nums):
		if len(nums)==1:
			return [nums]
		result = []
		for i in range(len(nums)):
			if i>=1 and nums[i]==nums[i-1]:
				continue
			newnums = nums[0:i]+nums[i+1:]
			permute = self.help(newnums)
			for j in permute:
				j.insert(0,nums[i])
				result.append(j)
		return result
	def permuteUnique(self,nums):
		if len(nums)==0:
			return []
		if len(nums)==1:
			return [nums]
		nums.sort()
		return self.help(nums)
s = Solution()
nums = [1,1,2]
print s.permuteUnique(nums)
