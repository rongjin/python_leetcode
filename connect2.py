class TreeLinkNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None
	
class Solution(object):
	def connect(self,root):
		if root == None:
			return
		mystack = []
		mystack.append(root)
		mystack.append(None)
		prev = None
		while(len(mystack)!=0):
			top = mystack.pop(0)
			if top!=None:
				if top.left:
					mystack.append(top.left)
				if top.right:
					mystack.append(top.right)
				if prev !=None:
					prev.next = top
					print prev.val,top.val
				prev = top
			elif top == None:
				if prev != None:
					mystack.append(None)
				prev = top




mylist = []
mylist.append(TreeLinkNode(1))
mylist.append(TreeLinkNode(2))
mylist.append(TreeLinkNode(3))
mylist.append(TreeLinkNode(4))
mylist.append(TreeLinkNode(5))
mylist.append(TreeLinkNode(7))
mylist[0].left = mylist[1]
mylist[0].right = mylist[2]
mylist[1].left = mylist[3]
mylist[1].right = mylist[4]
mylist[2].right = mylist[5]
s = Solution()
s.connect(mylist[0])
print mylist[3].next.val
print mylist[4].next.val
