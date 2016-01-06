class Solution(object):
	def subsets(self,nums):
		if nums == []:
			return [[]]
		elif len(nums)==1:
			return [[],nums]
		else:
			nums.sort()
			mylist = []
			result = self.subsets(nums[1:])
			for i in result:
				j = []
				for k in i:
					j.append(k)
				j.insert(0,nums[0])
				mylist.append(j)
				mylist.append(i)
			return mylist

s = Solution()
nums = [1,2,4]
result = s.subsets(nums)
for i in result:
	print i
