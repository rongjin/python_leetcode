class Solution(object):
	def convertToTitle(self,n):
		result = ""
		while(n>0):
			d = (n-1)%26
			n = (n-1)/26
			result = chr(ord('A')+d)+result
		return result

s = Solution()
n = 29
print s.convertToTitle(n)
