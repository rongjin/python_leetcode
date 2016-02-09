class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def minDepth(self, root):
		if root==None:
			return 0
		elif root.left == None and root.right == None:
			return 1
		elif root.left == None:
			return self.minDepth(root.right)+1
		elif root.right == None:
			return self.minDepth(root.left)+1
		else:
			l = self.minDepth(root.left)
			r = self.minDepth(root.right)
			return min(l,r)+1
