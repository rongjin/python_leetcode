class Solution(object):
	def plusOne(self, digits):
		dig = []
		l = len(digits)
		for i in range(l):
			dig.append(digits[l-1-i])
		extra = 1
		newdig = []
		for i in range(l):
			num = dig[i]+extra
			extra = num/10
			newdig.append(num%10)
		if extra!=0:
			newdig.append(extra)
		result = []
		l = len(newdig)
		for i in range(l):
			result.append(newdig[l-1-i])
		return result

s = Solution()
digits = []
print digits
print s.plusOne(digits)
