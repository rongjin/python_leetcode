class Solution(object):
	def __init__(self):
		self.mydict = {"2":"abc","3":"def","4":"ghi","5":"jkl",\
				"6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
	def help(self,digit,stack):
		newstack = []
		for i in stack:
			letters = self.mydict[digit]
			for j in letters:
				newstack.append(i+j)
		return newstack
	def letterCombinations(self,digits):
		if digits == "":
			return []
		result = [""]
		for i in digits:
			newresult = self.help(i,result)
			result = newresult
		print result
		return result

digits = "2"
s = Solution()
s.letterCombinations(digits)
