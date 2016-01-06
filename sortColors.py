class Solution(object):
	def sortColors(self,nums):
		mylist = [0,0,0]
		for i in nums:
			mylist[i] += 1
		k = 0
		for i in range(len(mylist)):
			for j in range(mylist[i]):
				nums[k] = i
				k += 1
		print nums

s = Solution()
nums = [0,1,0,1,2,2,0,1]
s.sortColors(nums)
