class Solution(object):
	def containDuplicate(self,nums):
		mydict = {}
		for i in nums:
			if i in mydict:
				return True
			else:
				mydict[i] = 1
		return False

s = Solution()
nums = [1,2,1,3]
print s.containDuplicate(nums)
