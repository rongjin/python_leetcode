class Solution(object):
	def next(self,mystr):
		i = 0
		k = 1
		result = ""
		while(i<len(mystr)):
			while(i+1<len(mystr) and mystr[i]==mystr[i+1]):
				i+=1
				k+=1
			result += str(k)
			result += str(mystr[i])
			i+=1
			k = 1
		return result
			
	def countAndSay(self, n):
		mystr = "1"
		for i in range(n-1):
			mystr = self.next(mystr)
			print mystr
		return mystr

s = Solution()
print s.countAndSay(5)
