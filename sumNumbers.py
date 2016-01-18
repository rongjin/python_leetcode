class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.sum = 0
	def help(self,root,cur):
		if root.left == None and root.right == None:
			mysum = 0
			i=0
			while(i<len(cur)):
				mysum = mysum*10+cur[i]
				i+=1
			mysum = 10*mysum+root.val
			print mysum
			self.sum += mysum
		else:
			print root.val
			cur.append(root.val)
			if root.left:
				self.help(root.left,cur)
			if root.right:
				self.help(root.right,cur)
			cur.pop()
	def sumNumbers(self, root):
		if root == None:
			return 0
		cur = []
		self.help(root,cur)
		return self.sum

s = Solution()
mylist = []
mylist.append(TreeNode(1))
mylist.append(TreeNode(2))
mylist.append(TreeNode(3))
mylist[0].left = mylist[1]
mylist[0].right = mylist[2]
print s.sumNumbers(mylist[0])
