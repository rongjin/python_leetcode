class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def help(self,head,x,l1,l2,p,q):
		print head.val
		if head.val<x:
			p.next = ListNode(head.val)
			p = p.next
		else:
			q.next = ListNode(head.val)
			q = q.next
		if head.next:
			self.help(head.next,x,l1,l2,p,q)

	def partition(self,head,x):
		if head==None:
			return None
		l1 = ListNode(-1)
		l2 = ListNode(-1)
		p = l1
		q = l2
		self.help(head,x,l1,l2,p,q)
		p = l1
		while(p.next):
			p = p.next
		p.next = l2.next
		return l1.next

mylist = []
mylist.append(ListNode(1))
mylist.append(ListNode(4))
mylist.append(ListNode(3))
mylist.append(ListNode(2))
mylist.append(ListNode(5))
mylist.append(ListNode(2))
n = len(mylist)-1
for i in range(0):
	mylist[i].next = mylist[i+1]
s = Solution()
newhead = s.partition(mylist[0],3)
print
while(newhead):
	print newhead.val
	newhead = newhead.next
