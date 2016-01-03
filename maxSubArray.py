class Solution(object):
	def maxSubArray(self,nums):
		largest = -10000
		mylist = [nums[0]]
		for i in range(1,len(nums)):
			if mylist[i-1]<0:
				mylist.append(nums[i])
			else:
				mylist.append(nums[i]+mylist[i-1])
		for i in mylist:
			if i>largest:
				largest = i
		return largest

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
print s.maxSubArray(nums)

