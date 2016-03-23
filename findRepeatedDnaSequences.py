class Solution(object):
	def findRepeatedDnaSequences(self,s):
		l = len(s)
		result = []
		mydict = {}
		for i in range(l-10+1):
			cur = s[i:i+10]
			if cur in mydict:
				if mydict[cur] == 1:
					result.append(cur)
				mydict[cur] += 1
			else:
				mydict[cur] = 1
		print result
		return result

s = Solution()
mystr = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s.findRepeatedDnaSequences(mystr)
