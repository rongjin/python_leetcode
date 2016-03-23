class Solution(object):
	def reverse(self,nums,l,r):
		for i in range((r-l)/2):
			nums[l+i],nums[r-1-i] = nums[r-1-i],nums[l+i]
	def rotate(self,nums,k):
		l = len(nums)
		k = k%l
		self.reverse(nums,0,l-k)
		self.reverse(nums,l-k,l)
		self.reverse(nums,0,l)
		print nums

s = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
s.rotate(nums,3)
