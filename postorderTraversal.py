class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.result = []
	def postorderTraversal(self,root):
		if root == None:
			return []
		if root.left:
			self.postorderTraversal(root.left)
		if root.right:
			self.postorderTraversal(root.right)
		self.result.append(root.val)
		return self.result

s = Solution()
mylist = []
for i in range(3):
	mylist.append(TreeNode(i+1))
mylist[0].right = mylist[1]
mylist[1].left = mylist[2]
result = s.postorderTraversal(mylist[0])
print result
