class Solution(object):
	def help(self,nums,target,l,r):
		print l,r
		#find nums[l]=target
		#find nums[l]>target
		if r==l:
			return l
		if r-l==1:
			if target<=nums[l]:
				return l
			else:
				return r
		mid = (l+r)/2
		if nums[mid] == target:
			return mid
		elif nums[mid]<target:
			return self.help(nums,target,mid+1,r)
		else:
			return self.help(nums,target,l,mid)
	def searchInsert(self,nums,target):
		if target<=nums[0]:
			return 0
		elif target>nums[len(nums)-1]:
			return len(nums)
		else:
			return self.help(nums,target,0,len(nums))

s = Solution()
nums = [1,3,5]
target = 5
print nums
print target
print s.searchInsert(nums,target)
