class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution(object):
	def reverse(self,head):
		if(head == None or head.next == None):
			return head
		p = head
		q = head.next
		newhead = self.reverse(q)
		q.next = p
		p.next = None
		return newhead
	def reverseKGroup(self,head,k):
		if head == None:
			return head
		if k==1:
			return head
		p = head
		for i in range(k-1):
			if p:
				p = p.next
		if p==None:
			return head
		else:
			q = p.next
			p.next = None
			newhead = self.reverse(head)
			head.next = self.reverseKGroup(q,k)
			return newhead

mylist = [1,2,3,4,5]
head = ListNode(-1)
p = head
for i in range(len(mylist)):
	p.next = ListNode(mylist[i])
	p = p.next
p = head.next
while(p):
	print p.val
	p = p.next
s = Solution()
newhead = s.reverseKGroup(head.next,2)
while(newhead):
	print newhead.val
	newhead = newhead.next
