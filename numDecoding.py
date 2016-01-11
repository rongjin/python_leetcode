class Solution(object):
	def __init__(self):
		self.mydict = {'1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G',\
				'8':'H','9':'I','10':'J','11':'K','12':'L','13':'M','14':'N',\
				'15':'O','16':'P','17':'Q','18':'R','19':'S','20':'T',\
				'21':'U','22':'V','23':'W','24':'X','25':'Y','26':'Z'}
		self.record = {}

	def numDecodings(self,s):
		print s
		if len(s)==0:
			return 0
		elif len(s)==1:
			if s in self.mydict:
				return 1
			return 0
		else:
			result = 0
			if (s[0]) in self.mydict:
				if len(s[1:])==0:
					result += 1
				elif s[1:] in self.record:
					result += self.record[s[1:]]
				else:
					d = self.numDecodings(s[1:])
					self.record[s[1:]] = d
					result += d
			if (s[0:2])in self.mydict:
				if len(s[2:])==0:
					result += 1
				elif s[2:] in self.record:
					result += self.record[s[2:]]
				else:
					d = self.numDecodings(s[2:])
					self.record[s[2:]] = d
					result += d
			print s,result
			return result

mystr = "12"
s = Solution()
print s.numDecodings(mystr)
