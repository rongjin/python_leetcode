class Solution(object):
	def isIsomorphic(self,s,t):
		if len(s)!=len(t):
			return False
		i = 0
		mydict = {}
		mydict2 = {}
		for i in range(len(s)):
			if s[i] in mydict:
				if mydict[s[i]]!=t[i]:
					return False
			elif t[i] in mydict2:
				if mydict2[t[i]]!=s[i]:
					return False
			else:
				mydict[s[i]] = t[i]
				mydict2[t[i]] = s[i]
			print mydict
		return True

s = Solution()
mys = "ab"
myt = "aa"
print s.isIsomorphic(mys,myt)
