class Solution(object):
	def titleToNumber(self,s):
		result = 0
		while(s):
			c = s[0]
			s = s[1:]
			result = result*26+ (ord(c)-ord('A')+1)
		return result

s = Solution()
print s.titleToNumber("AB")

