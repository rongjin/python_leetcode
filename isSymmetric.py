class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def help(self,left, right):
		if left == None and right == None:
			return True
		elif left == None:
			return False
		elif right == None:
			return False
		else:
			if left.val != right.val:
				return False
			if self.help(left.left,right.right) == False:
				return False
			if self.help(left.right,right.left) == False:
				return False
			return True

	def isSymmetric(self,root):
		if root == None:
			return True
		return self.help(root.left,root.right)
