class Solution(object):
	def majorityElement(self,nums):
		mydict = {}
		for i in nums:
			if i not in mydict:
				mydict[i] = 1
			else:
				mydict[i]+=1
			if mydict[i]>len(nums)/2:
				return i

