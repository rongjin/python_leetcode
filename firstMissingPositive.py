class Solution(object):
	def swap(self,nums,i,j):
		temp = nums[i]
		nums[i] = nums[j]
		nums[j] = temp
	def firstMissingPositive(self,nums):
		if nums == []:
			return 1
		for i in range(len(nums)):
			while nums[i]>0 and i+1!=nums[i] and nums[i]<=len(nums):
				j = nums[i]-1
				if nums[i]!=nums[j]:
					self.swap(nums,i,j)
				else:
					break
				print nums
		for i in range(len(nums)):
			if i+1!=nums[i]:
				return i+1
		return len(nums)+1
s = Solution()
#nums=[1,2,0]
nums = [3,4,-1,1]
nums = [1,2]
print s.firstMissingPositive(nums)
