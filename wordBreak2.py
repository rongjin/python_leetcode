class Solution(object):
	def __init__(self):
		self.result = {}

	def help(self,s,l,r,wordDict):
		if s[l:r] in self.result:
			return self.result[s[l:r]]
		#print s[l:r],l,r
		if s[l:r] in wordDict:
			result = [[s[l:r]]]
		else:
			result = []
		for i in range(1,r-l):
			if s[l:(l+i)] in wordDict:
				result2 = self.help(s,l+i,r,wordDict)
				if result2 == []:
					continue
				for j in result2:
					d = [s[l:(l+i)]]
					for jj in j:
						d.append(jj)
					if d not in result:
						result.append(d)
		self.result[s[l:r]] = result
		print s[l:r],result
		return result
	def wordBreak(self,s,wordDict):
		result = self.help(s,0,len(s),wordDict)
		myreturn = []
		for i in result:
			mys = ""
			for j in i:
				mys += j+" "
			myreturn.append(mys[0:len(mys)-1])
		return myreturn

s = Solution()
mystr = "catsanddog"
mydict = ["cat","cats","and","sand","dog"]
#mystr = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#mydict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
result = s.wordBreak(mystr,mydict)
for i in result:
	print i
