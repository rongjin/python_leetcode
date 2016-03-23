class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.result = []
	def help(self,root,level):
		if level==len(self.result):
			self.result.append(root.val)
		if root.right:
			self.help(root.right,level+1)
		if root.left:
			self.help(root.left,level+1)

	def rightSideView(self,root):
		if root == None:
			return self.result
		self.help(root,0)
		return self.result

s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
print s.rightSideView(node1)



