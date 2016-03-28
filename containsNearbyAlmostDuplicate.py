import sys
class Solution(object):
	def containsNearbyAlmostDuplicate(self,nums,k,t):
		if k<0 or t<0:
			return False
		mydict = {}
		mymin = -sys.maxint-1
		for i in range(len(nums)):
			bucket = (nums[i]-mymin)/(t+1)
			print bucket
			if bucket in mydict:
				return True
			else:
				if bucket-1 in mydict and abs(nums[i]-mydict[bucket-1])<=t:
					return True
				if bucket+1 in mydict and abs(nums[i]-mydict[bucket+1])<=t:
					return True
			mydict[bucket] = nums[i]
			if len(mydict)>=k+1:
				bucket2 = (nums[i-k]-mymin)/(t+1)
				print mydict
				print bucket2
				del mydict[bucket2]
			print mydict
		return False
s = Solution()
nums = [4,2]
k = 2
t = 1
print s.containsNearbyAlmostDuplicate(nums,k,t)

