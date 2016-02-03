class Solution(object):
	def lengthOfLastWord(self,s):
		if s =="":
			return 0
		if len(s)==1 and s.isalpha():
			return s
		i = len(s)-1
		while(i>=0 and s[i].isalpha()==False):
			i-=1
		print i
		if i<0:
			return 0
		else:
			j = i
			while(j>=0 and s[j].isalpha()):
				j-=1
			return i-j

s = Solution()
mystr = "Hello World!"
print s.lengthOfLastWord(mystr)
