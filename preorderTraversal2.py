class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def inorderTraversal(self,root):
		if root == None:
			return []
		mystack = []
		result = []
		mystack.append(root)
		while(mystack!=[]):
			top = mystack.pop()
			result.append(top.val)
			if top.right:
				mystack.append(top.right)
			if top.left:
				mystack.append(top.left)
		return result

mylist = []
for i in range(7):
	mylist.append(TreeNode(i+1))
mylist[0].right = mylist[1]
mylist[1].left = mylist[2]
mylist[1].right = mylist[3]
mylist[2].left = mylist[4]
mylist[2].right = mylist[5]
s = Solution()
print s.inorderTraversal(mylist[0])
