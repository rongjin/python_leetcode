class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def inorderTraversal(self,root):
		if root == None:
			return []
		result = []
		if root.left:
			result += self.inorderTraversal(root.left)
		result += [root.val]
		if root.right:
			result += self.inorderTraversal(root.right)
		return result

mylist =[]
for i in range(3):
	mylist.append(TreeNode(i+1))
mylist[0].right = mylist[1]
mylist[1].left = mylist[2]
s = Solution()
print s.inorderTraversal(mylist[0])
