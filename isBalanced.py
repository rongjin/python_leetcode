class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def help(self,root):
		if root == None:
			return 0
		else:
			l = self.help(root.left)
			r = self.help(root.right)
			if l==-1 or r==-1 or abs(l-r)>1:
				return -1
			else:
				return max(l,r)+1

	def isBalanced(self,root):
		if root == None:
			return True
		d = self.help(root)
		if d == -1:
			return False
		else:
			return True
