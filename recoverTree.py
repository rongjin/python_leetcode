class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def recoverTree(self,root):
		mystack = []
		mylist = []
		first = None
		second = None
		p = root
		while(p.left):
			mystack.append(p)
			p = p.left
		mystack.append(p)
		while(mystack!=[]):
			top = mystack.pop()
			if mylist!=[] and top.val<mylist[-1].val:
				if first ==None:
					first = mylist[-1]
					second = top
				else:
					second = top
			mylist.append(top)
			if top.right!=None:
				p = top.right
				while p.left:
					mystack.append(p)
					p = p.left
				mystack.append(p)
		first.val,second.val = second.val,first.val
		for i in mylist:
			print i.val
mylist = []
mylist.append(TreeNode(1))
mylist.append(TreeNode(2))
mylist.append(TreeNode(3))
mylist[2].left = mylist[0]
mylist[2].right = mylist[1]
s = Solution()
s.recoverTree(mylist[2])

