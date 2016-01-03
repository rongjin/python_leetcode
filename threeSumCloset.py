class Solution(object):
	def threeSumCloset(self,nums,target):
		nums.sort()
		mymin = 10000
		i = 0;
		while i<len(nums)-2:
			j = i+1
			k = len(nums)-1
			while (j<k):
				mysum = nums[i]+nums[j]+nums[k]
				if mysum == target:
					return target
				else:
					if abs(mysum-target)<mymin:
						mymin = abs(mysum-target)
						result = mysum
					if mysum<target:
						j+=1
					else:
						k-=1
			i+=1
		return result

s = Solution()
nums = [-1,2,1,-4]
target = 1
print s.threeSumCloset(nums,1)

