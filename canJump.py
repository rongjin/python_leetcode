class Solution(object):
	def canJump(self,nums):
		if len(nums)==1:
			return True
		mylist = [1]
		for i in range(len(nums)):
			print mylist
			if len(mylist)-1<i:
				return False
			maxl = i+nums[i]
			print maxl
			if maxl >= len(nums)-1:
				return True
			if maxl > len(mylist)-1:
				for j in range(len(mylist),maxl+1):
					mylist.append(1)

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
nums = [0,1]
nums = [1,2,3]
s = Solution()
print s.canJump(nums)

