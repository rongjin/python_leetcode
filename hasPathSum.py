class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	

class Solution(object):
	def hasPathSum(self,root,sum):
		if root==None:
			return False
		elif root.left == None and root.right == None:
			if root.val == sum:
				return True
			else:
				return False
		else:
			if root.left:
				l = self.hasPathSum(root.left,sum-root.val)
				if l:
					return True
			if root.right:
				r = self.hasPathSum(root.right,sum-root.val)
				if r:
					return True
			return False
