import math
import sys

class Solution(object):
	def maximumGap(self,nums):
		if len(nums)<2:
			return 0
		elif len(nums)==2:
			return max(nums)-min(nums)
		n = len(nums)
		print "l",n
		mymin = min(nums)
		mymax = max(nums)
		gap = int((mymax-mymin)/(n-1))+1;
		print mymax,mymin,n-1,gap
		if gap==0:
			return 0
		print "gap",gap
		mat = [[sys.maxint,-sys.maxint-1] for i in range(n)]
		print len(mat)
		for i in range(0,n):
			if nums[i]!=mymin and nums[i]!=mymax:
				gapindex = (nums[i]-mymin)/gap
				print "index",gapindex
				if nums[i]<mat[gapindex][0]:
					mat[gapindex][0] = nums[i]
				if nums[i]>mat[gapindex][1]:
					mat[gapindex][1] = nums[i]
		maxgap = 0
		prev = mymin
		for i in range(n):
			if mat[i][0]!=sys.maxint:
				if mat[i][0]-prev>maxgap:
					maxgap = mat[i][0]-prev
				prev = mat[i][1]
				print "prev",prev
		if mymax-prev>maxgap:
			maxgap = mymax-prev
		return maxgap



s = Solution();
nums = [3,6,9,1]
print nums
print s.maximumGap(nums);

