class Solution(object):
	def help(self,nums,l,r):
		print l,r
		if r-l<2:
			return nums[l]
        elif r-l==2:
            return min(nums[l],nums[l+1])
		else:
			if nums[r-1]>nums[l]:
				return nums[l]
			while(l+1<r and nums[l]==nums[l+1]):
				l+=1
			if r-l<2:
				return nums[l]
			else:
				mid = (l+r)/2
				if nums[mid]>nums[l]:
					return self.help(nums,mid+1,r)
				else:
					return self.help(nums,l,mid+1)


	def findMin(self,nums):
		return self.help(nums,0,len(nums))


s = Solution()
nums = [1,1,3]
nums = [4,5,0,1,2]
print nums
print s.findMin(nums)

