class Solution(object):
	def isPalindrome(self, s):
		if s == "":
			return True
		i = 0
		j = len(s)-1
		while(i<j):
			while(i<j and s[i].isalnum()==False):
				i+=1
			if i==j:
				return True
			while(i<j and s[j].isalnum()==False):
				j-=1
			if i==j:
				return True
			if s[i].lower() == s[j].lower():
				i+=1
				j-=1
			else:
				return False
		return True

s = Solution()
mystr = "A man, a plan, a canal: Panama"
mystr = "race a car"
mystr = "! "
print s.isPalindrome(mystr)

