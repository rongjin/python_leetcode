class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def invertTree(self,root):
		if root == None:
			return root
		right2 = self.invertTree(root.left)
		left2 = self.invertTree(root.right)
		root.left = left2
		root.right = right2
		return root
