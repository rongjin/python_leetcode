class Solution(object):
	def jump(self,nums):
		l = len(nums)
		if l<2:
			return 0
		mylist = [-1 for i in range(l)]
		mylist[0] = 0
		far = 0
		for i in range(len(nums)):
			cur = i
			far2 = i+nums[i]
			if far2>=len(nums)-1:
				return mylist[i]+1
			if far2 > far:
				for j in range(far+1,far2+1):
					mylist[j] = mylist[i]+1
				far = far2
			#print mylist

s = Solution()
nums = [1,1,1,1,1]
#print nums
print s.jump(nums)
