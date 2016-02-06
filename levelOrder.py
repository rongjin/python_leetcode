class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def help(self,root,level,result):
		if level>=len(result):
			result.append([])
		result[level].append(root.val)
		if root.left:
			self.help(root.left,level+1,result)
		if root.right:
			self.help(root.right,level+1,result)

	def levelOrder(self,root):
		result = []
		if root == None:
			return result
		self.help(root,0,result)
		return result

s = Solution()
node = TreeNode(1)
print s.levelOrder(node)
