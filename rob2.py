import sys
class Solution(object):
	def rob(self,nums):
		l = len(nums)
		if l==0:
			return 0
		mat = [[[0 for k in range(2)] for j in range(2)] for i in range(l)]
		print mat
		mat[0][1][1] = nums[0]
		for i in range(1,l-1):
			#tag as 0
			mat[i][0][0] = max(mat[i-1][0][0],mat[i-1][0][1])
			#tag as 1
			mat[i][0][1] = max(mat[i-1][0][0]+nums[i],-sys.maxint)
			#tag as 0
			mat[i][1][0] = max(mat[i-1][1][0],mat[i-1][1][1])
			#tag as 1
			if i==1:
				mat[i][1][1] = -sys.maxint
			else:
				mat[i][1][1] = max(mat[i-1][1][0]+nums[i],-sys.maxint)
			#print mat[i]
		#last tag as 0
		mat[l-1][0][0] = max(mat[l-2][0][0],mat[l-2][0][1])
		mat[l-1][0][1] = max(mat[l-2][0][0]+nums[l-1],-sys.maxint)
		mat[l-1][1][0] = max(mat[l-2][1][0],mat[l-2][1][1])
		mat[l-1][1][1] = -sys.maxint
		#print mat[l-1]
		mymax = max(mat[l-1][0][0],mat[l-1][0][1],mat[l-1][1][0])
		return mymax
s = Solution()
nums = [1,2]
print s.rob(nums)



