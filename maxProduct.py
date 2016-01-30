class Solution(object):
	def maxProduct(self,nums):
		l = len(nums)
		result = [[0 for i in range(2)] for i in range(l)]
		result[0][0] = nums[0]
		result[0][1] = nums[0]
		for i in range(1,l):
			if nums[i]==0:
				continue
			elif nums[i]>0:
				result[i][0] = max(nums[i],result[i-1][0]*nums[i])
				result[i][1] = min(nums[i],result[i-1][1]*nums[i])
			else:
				result[i][0] = max(nums[i],result[i-1][1]*nums[i])
				result[i][1] = min(nums[i],result[i-1][0]*nums[i])
		for i in range(l):
			print result[i][0],
		print
		for i in range(l):
			print result[i][1],
		print
		largest = -10000
		for i in range(l):
			if result[i][0]>largest:
				largest = result[i][0]
		return largest

s = Solution()
nums = [2,3,-2,-4]
nums = [-4,-3]
print s.maxProduct(nums)

