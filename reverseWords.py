class Solution(object):
	def reversestring(self,s):
		news = ""
		for i in range(len(s)):
			news += s[-1-i]
		return news
	def reverseWords(self,s):
		i = 0
		result = ""
		old= ""
		while(i<len(s)):
			if s[i]==" ":
				print old
				result += self.reversestring(old)
				result += " "
				old = ""
			else:
				old += s[i]
			i+=1
		if old:
			result += self.reversestring(old)
		print result
		return self.reversestring(result)

s = Solution()
mys = "the sky is blue"
print s.reverseWords(mys)


