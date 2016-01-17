class TreeLinkNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution(object):
	def connect(self,root):
		if root==None:
			return
		if root.left:
			root.left.next = root.right
			if root.next!=None:
				root.right.next = root.next.left
		self.connect(root.left)
		self.connect(root.right)

mylist = []
mylist.append(TreeLinkNode(1))
mylist.append(TreeLinkNode(2))
mylist.append(TreeLinkNode(3))
mylist[0].left = mylist[1]
mylist[0].right = mylist[2]
s = Solution()
s.connect(mylist[0])
print mylist[1].next.val

