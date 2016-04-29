class Solution(object):
	def summaryRanges(self,nums):
		result = []
		if len(nums)==0:
			return result
		i = 0
		j = 0
		while(i<len(nums)):
			j = i
			while(j+1<len(nums) and nums[j+1]==nums[j]+1):
				j += 1
			if i==j:
				result.append(str(nums[i]))
			else:
				result.append(str(nums[i])+"->"+str(nums[j]))
			i = j+1
		return result
		

s = Solution()
nums = [0,1,2,4,5,7]
print s.summaryRanges(nums)
