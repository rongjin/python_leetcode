class Solution(object):
	def help(self,nums,target,l,r):
		print l,r
		if r==l:
			return False
		elif r-l==1:
			if nums[l]!=target:
				return False
			else:
				return True
		else:
			while(r-l>1 and nums[l]==nums[l+1]):
				l+=1
			mid = (l+r)/2
			if nums[mid]==target:
				return True
			elif nums[mid]>nums[l]:
				if target>=nums[l] and target<nums[mid]:
					return self.help(nums,target,l,mid)
				else:
					return self.help(nums,target,mid+1,r)
			else:
				if target>nums[mid] and target<=nums[r-1]:
					return self.help(nums,target,mid+1,r)
				else:
					return self.help(nums,target,l,mid)

	def search(self,nums,target):
		return self.help(nums,target,0,len(nums))

nums = [5,5,6,7,1,2,3,4,5]
nums = [1,3,1,1,1]
target = 3
s = Solution()
print s.search(nums,target)
