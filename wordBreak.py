class Solution(object):
	def __init__(self):
		self.record = {}

	def help(self,s,l,r,wordDict):
		#print s[l:r],l,r
		if s[l:r] in self.record:
			return self.record[s[l:r]]
		if s[l:r] in wordDict:
			return True
		for i in range(1,r-l):
			#print i
			if s[l:(l+i)] in wordDict:
				if self.help(s,l+i,r,wordDict):
					return True
		self.record[s[l:r]] = False
		return False


	def wordBreak(self,s,wordDict):
		result = self.help(s,0,len(s),wordDict)
		return result

s = Solution()
mystr = "leetcode"
mydict = ["le","leet","code"]
mystr = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
mydict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s.wordBreak(mystr,mydict)
