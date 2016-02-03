class Solution(object):
	def removeElement(self,nums,val):
		i = 0
		j = 0
		while(j<len(nums)):
			if nums[j]!=val:
				nums[i] = nums[j]
				i+=1
			j+=1
		return i


nums = [1,2,3,2,5]
s = Solution()
s.removeElement(nums,2)
print nums
