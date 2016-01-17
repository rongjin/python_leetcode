class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def __init__(self):
		self.max = -10000
	def help(self,root):
		if root == None:
			return 0
		ll = self.help(root.left)
		rr = self.help(root.right)
		if max(0,ll)+max(0,rr)+root.val>self.max:
			self.max = max(0,ll)+max(0,rr)+root.val
			print root.val,ll,rr
		if max(ll,rr)<0:
			return root.val
		else:
			return max(ll,rr)+root.val

	def maxPathSum(self,root):
		if root == None:
			return 0
		self.help(root)
		return self.max

mylist = []
mylist.append(TreeNode(5))
mylist.append(TreeNode(4))
mylist.append(TreeNode(11))
mylist.append(TreeNode(8))
mylist.append(TreeNode(13))
mylist[0].left = mylist[1]
mylist[1].left = mylist[2]
mylist[0].right = mylist[3]
mylist[3].left = mylist[4]
s = Solution()
print s.maxPathSum(mylist[0])
