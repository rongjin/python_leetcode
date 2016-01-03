class Solution(object):
	def searchleft(self,nums,target,l,r):
		print l,r
		if r-l == 1:
			if nums[l]<target and nums[r-1]>target:
				return -1
			elif target<nums[l]:
				return -1
			elif target> nums[r-1]:
				return -1
		mid = (l+r)/2
		if nums[mid] < target:
			return self.searchleft(nums,target,mid+1,r)
		elif nums[mid] > target:
			return self.searchleft(nums,target,l,mid)
		elif nums[mid] == target:
			if mid-1>=0 and nums[mid-1]<target:
				return mid
			else:
				return self.searchleft(nums,target,l,mid)
	def searchright(self,nums,target,l,r):
		print l,r
		if r-l == 1:
			if nums[l]<target and nums[r-1]>target:
				return -1
			elif target>nums[r-1]:
				return -1
			elif nums[l]>target:
				return -1
		mid = (l+r)/2
		if nums[mid] < target:
			return self.searchright(nums,target,mid+1,r)
		elif nums[mid] > target:
			return self.searchright(nums,target,l,mid)
		elif nums[mid] == target:
			if mid+1<=len(nums)-1 and nums[mid+1]>target:
				return mid
			else:
				return self.searchright(nums,target,mid,r)
	def searchRange(self,nums,target):
		result = [-1,-1]
		if target<nums[0] or target>nums[len(nums)-1]:
			return result
		if nums[0] == target:
			result[0] = 0
		else:
			result[0] = self.searchleft(nums,target,0,len(nums))
		if nums[len(nums)-1]==target:
			result[1] = len(nums)-1
		else:
			result[1] = self.searchright(nums,target,0,len(nums))
		return result

s = Solution()
nums = [1,2,3]
target = 3
print s.searchRange(nums,target)
