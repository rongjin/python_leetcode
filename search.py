class Solution(object):
	def help(self,nums,target,begin,end):
		#basic case
		print begin,end
		if begin==end:
			return -1
		if(end-begin == 1):
			if target!=nums[begin]:
				return -1
			else:
				return begin
		mid = (begin + end)/2
		#print mid
		if nums[mid]==target:
			return mid
		elif nums[mid]>nums[begin]:
			if target>=nums[begin] and target<nums[mid]:
				return self.help(nums,target,begin,mid)
			else:
				return self.help(nums,target,mid+1,end)
		elif nums[mid]<nums[begin]:
			if target<=nums[end-1] and target>nums[mid]:
				return self.help(nums,target,mid+1,end)
			else:
				return self.help(nums,target,begin,mid)
	def search(self,nums,target):
		return self.help(nums,target,0,len(nums))

s = Solution()
nums = [4,5,6,7,0,1,2,3]
target = 2
print s.search(nums,target)
