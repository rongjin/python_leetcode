class Solution(object):
	def removeDuplicates(self,nums):
		result = 1
		if(len(nums)<2):
			return(len(nums))
		i = 0
		j = 1
		while(j<len(nums)):
			if(nums[i]==nums[j]):
				j+=1
			else:
				nums[i+1] = nums[j]
				i += 1
				j += 1
				result += 1
		print nums
		return result

s = Solution()
nums = [1,1,2,3,3]
print s.removeDuplicates(nums)
