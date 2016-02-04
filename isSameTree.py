class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		if p==None and q==None:
			return True
		elif p==None:
			return False
		elif q == None:
			return False
		else:
			if p.val!=q.val:
				return False
			elif self.isSameTree(p.left,q.left)==False:
				return False
			elif self.isSameTree(p.right,q.right)==False:
				return False
			return True
		return True

s = Solution()
a = TreeNode(1)
b = TreeNode(1)
print s.isSameTree(a,b)
