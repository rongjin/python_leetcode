class Solution(object):
	def __init__(self):
		self.mydict = {}
	def help(self,s,l,r):
		d = 1
		while(l-d>=0 and r+d-1<len(s) and s[l-d]==s[r+d-1]):
			self.mydict[(l-d,r+d)]=1
			d+=1
	def part(self,s,l,r):
		#print "part",s[l:r]
		if r==l:
			return [[]]
		elif r-l==1:
			return [[s[l]]]
		else:
			result = []
			for i in range(1,r-l+1):
				if (l,l+i) in self.mydict:
					value = []
					value.append(s[l:l+i])
					result2 = self.part(s,l+i,r)
					for k in result2:
						result.append([])
						result[-1].append(s[l:(l+i)])
						for kk in k:
							result[-1].append(kk)
			print "@\n",s[l:r],result
			return result

	def partition(self,s):
		for i in range(len(s)):
			self.mydict[(i,i+1)]=1
			self.help(s,i,i+1)
			if i+1<len(s) and s[i]==s[i+1]:
				self.mydict[(i,i+2)]=1
				self.help(s,i,i+2)
		print self.mydict
		result = self.part(s,0,len(s))
		return result

s = Solution()
string = "aaabb"
result = s.partition(string)
print "##"
for i in result:
	print i
