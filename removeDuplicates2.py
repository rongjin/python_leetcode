class Solution(object):
	def removeDuplicates(self,nums):
		if len(nums)<=2:
			return len(nums)
		i = 0
		j = 1
		while(j<len(nums)):
			if nums[j]==nums[i]:
				if i==0 or nums[i]!=nums[i-1]:
					nums[i+1] = nums[i]
					i+=1
					j+=1
				else:
					j+=1
			else:
				nums[i+1] = nums[j]
				i+=1
				j+=1
		print nums
		return i+1

nums = [1,1,1,2,2,3,4,5,5]
s = Solution()
print nums
print s.removeDuplicates(nums)
