class Solution(object):
	def swap(self,nums,i,j):
		temp = nums[i]
		nums[i] = nums[j]
		nums[j] = temp
	def nextPermutation(self,nums):
		j = len(nums)-1
		while(j-1>=0 and nums[j]<=nums[j-1]):
			j -= 1
		if j==0:
			nums.sort()
		else:
			i = len(nums)-1
			while(nums[i]<=nums[j-1]):
				i-=1
			self.swap(nums,j-1,i)
			l = j
			r = len(nums)-1
			while(l<r):
				self.swap(nums,l,r)
				l+=1
				r-=1
		print nums

s = Solution()
s.nextPermutation([4,3,2,1])

