class Solution(object):
	def help(self,x,low,high):
		mid = (low+high)/2
		print low,high,mid
		while(high-low>1):
			if mid*mid==x:
				return mid
			elif mid*mid>x:
				return self.help(x,low,mid)
			else:
				return self.help(x,mid,high)
		return low
		if low==high:
			return low
	def mySqrt(self,x):
		if x==0:
			return 0
		elif x==1:
			return 1
		else:
			return self.help(x,1,x)
	
s = Solution()
print s.mySqrt(255)
