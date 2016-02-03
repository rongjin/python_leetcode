class Solution(object):
	def addBinary(self,a,b):
		i = len(a)-1
		j = len(b)-1
		result = []
		extra = 0
		while(i>=0 or j>=0):
			if i<0:
				num = int(b[j])+extra
				j-=1
			elif j<0:
				num = int(a[i])+extra
				i-=1
			else:
				num = int(a[i])+int(b[j])+extra
				i-=1
				j-=1
			extra = num/2
			result.append(num&1)
		if extra:
			result.append(extra)
		mystr = ""
		for i in range(len(result)):
			mystr+=str(result[len(result)-1-i])
		return mystr

s = Solution()
a = "11"
b = "1"
print s.addBinary(a,b)
