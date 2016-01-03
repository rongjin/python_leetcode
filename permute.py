class Solution(object):
	def permute(self,nums):
		if len(nums)==0:
			return []
		if len(nums)==1:
			return [nums]
		result = []
		for i in range(len(nums)):
			newnums = nums[:i]+nums[i+1:]
			newpermute = self.permute(newnums)
			for j in newpermute:
				j.insert(0,nums[i])
				result.append(j)
		return result

s = Solution()
nums = [1,2,3]
print s.permute(nums)
