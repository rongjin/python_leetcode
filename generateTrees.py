class TreeNode(object):
	def __init__(self,x):
		self.val = val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def help(self,m,n):
		if m==n:
			return []
		elif m==n-1:
			return [TreeNode(m)]
		else:
			result = []
			for i in range(m,n):
				root = TreeNode(i)
				leftresult = self.help(m,i)
				rightresult = self.help(i+1,n)
				if leftresult == []:
					for jj in rightresult:
						newnode = TreeNode(i)
						newnode.right = jj
						result.append(newnode)
				elif rightresult == []:
					for ii in leftresult:
						newnode = TreeNode(i)
						newnode.left = ii
						result.append(newnode)
				else:
					for ii in leftresult:
						for jj in rightresult:
							newnode = TreeNode(i)
							newnode.left = ii
							newnode.right = jj
							result.append(newnode)
			return result
	def generateTrees(self,n):
		result = self.help(1,n+1)
		return result

s = Solution()
result = s.generateTrees(3)
for i in result:
	print i.val
