class Solution(object):
	def minSubArrayLen(self,s,nums):
		i = 0
		j = 0
		mysum = 0
		minl = 10000
		while(j<len(nums)):
			if j<len(nums):
				mysum += nums[j]
				j += 1
			while(j<len(nums) and mysum<s):
				mysum += nums[j]
				j += 1
			while(mysum-nums[i]>=s):
				mysum -= nums[i]
				i +=1
			print i,j,nums[i:j]
			if mysum>=s and j-i<minl:
				minl = j-i
		if minl == 10000:
			minl = 0
		return minl

s = Solution()
summ = 7
nums = [2,3,1,2,4,3]
print nums
print s.minSubArrayLen(summ,nums)

