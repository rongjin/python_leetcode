class Solution(object):
	def fourSum(self,nums,target):
		if(len(nums)<4):
			return []
		nums.sort()
		result = []
		i = 0
		while(i<len(nums)-3):
			if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
				break
			j = len(nums)-1
			while(i<j):
				ii = i+1;
				jj = j-1;
				while(ii<jj):
					mysum = nums[i]+nums[j]+nums[ii]+nums[jj]
					if mysum == target:
						result.append([nums[i],nums[ii],nums[jj],nums[j]])
						ii+=1
						while(ii<len(nums) and nums[ii]==nums[ii-1]):
							ii+=1
						jj-=1
						while(jj>0 and nums[jj]==nums[jj+1]):
							jj-=1
					elif mysum < target:
						ii+=1
						while(ii<len(nums) and nums[ii]==nums[ii-1]):
							ii+=1
					else:
						jj-=1
						while(jj>0 and nums[jj]==nums[jj+1]):
							jj-=1
				j-=1;
				while(j>0 and nums[j]==nums[j+1]):
					j-=1
			i+=1
			while(i<len(nums) and nums[i]==nums[i-1]):
				i+=1
		print result
		return result

s = Solution()
nums = [-5,5,4,-3,0,0,4,-2]
target = 4
s.fourSum(nums,target)
