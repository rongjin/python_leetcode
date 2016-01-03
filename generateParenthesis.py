class Solution(object):
	def __init__(self):
		self.result = []
	def help(self,cur,n,left,right):
		if left == n and right == n:
			self.result.append(cur)
		elif left == n:
			self.help(cur+")",n,left,right+1)
		elif left == right:
			self.help(cur+"(",n,left+1,right)
		else:
			self.help(cur+"(",n,left+1,right)
			self.help(cur+")",n,left,right+1)
	def generateParenthesis(self,n):
		if n==0:
			return []
		cur = ""
		self.help(cur,n,0,0)
		return self.result

s = Solution()
print s.generateParenthesis(3)
