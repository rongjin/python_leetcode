class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.stack = []

class BSTIterator(object):
	def __init__(self,root):
		if root:
			self.stack = [root]
			while(root.left):
				self.stack.append(root.left)
				root = root.left
		else:
			self.stack = []

	def hasNext(self):
		if len(self.stack)>0:
			return True
		else:
			return False
	
	def next(self):
		if self.stack!=[]:
			top = self.stack.pop()
			if top.right:
				self.stack.append(top.right)
				d = top.right
				while(d.left):
					self.stack.append(d.left)
					d = d.left
			return top.val


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
i,v = BSTIterator(root),[]
while i.hasNext():
	v.append(i.next())
print v
