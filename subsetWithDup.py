class Solution(object):
	def subsetsWithDup(self,nums):
		if len(nums)==0:
			return [[]]
		if len(nums)==1:
			return [[],nums]
		same = 0
		while(same<len(nums)-1 and nums[same]==nums[same+1]):
			same+=1
		result = self.subsetsWithDup(nums[same+1:])
		newresult = []
		for i in result:
			for k in range(same+2):
				cur = []
				for j in i:
					cur.append(j)
				for j in range(k):
					cur.insert(0,nums[0])
				newresult.append(cur)
		return newresult


nums = [1,2,2]
s = Solution()
r = s.subsetsWithDup(nums)
print "a"
for i in r:
	print i
