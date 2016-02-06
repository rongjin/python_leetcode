class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		if root == None:
			return 0
		else:
			l = self.maxDepth(root.left)
			r = self.maxDepth(root.right)
			return max(l,r)+1
