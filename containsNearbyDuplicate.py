class Solution(object):
	def containsNearbyDuplicate(self,nums,k):
		mydict = {}
		for i in range(len(nums)):
			if nums[i] not in mydict:
				mydict[nums[i]] = i
			else:
				if i-mydict[nums[i]]<=k:
					return True
				else:
					mydict[nums[i]] = i
		return False

s = Solution()
nums = [1,2,1]
print s.containsNearbyDuplicate(nums,1)

