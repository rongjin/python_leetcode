class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findmid(self,head):
		p = head
		q = head.next.next.next
		while(q and q.next):
			p = p.next
			q = q.next.next
		return p
	def sortedListToBST(self,head):
		if head == None:
			return None
		elif head.next == None:
			return TreeNode(head.val)
		elif head.next.next == None:
			root =TreeNode(head.val)
			root.right = TreeNode(head.next.val)
			return root
		mid = self.findmid(head)
		print mid.val
		root = TreeNode(mid.next.val)
		if mid.next and mid.next.next:
			right = self.sortedListToBST(mid.next.next)
		else:
			right = None
		mid.next = None
		left = self.sortedListToBST(head)
		root.left = left;
		root.right = right
		return root

mylist = []
for i in range(2):
	mylist.append(ListNode(i+1))
for i in range(1):
	mylist[i].next = mylist[i+1]
s = Solution()
result = s.sortedListToBST(mylist[0])
print result.val
print result.left
