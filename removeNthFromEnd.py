class ListNode(object):
	def __init__(self,x):
		self.val = x;
		self.next = None

class Solution(object):
	def removeNthFromEnd(self,head,n):
		if(n==0):
			return head
		if head==None:
			return head
		p = head
		q = head
		for i in range(n):
			if(p):
				p = p.next
		if p==None:
			return head.next
		while(p.next!=None):
			p = p.next
			q = q.next
		if q.next:
			q.next = q.next.next
		else:
			q.next = None
		return head

head = ListNode(1)
p = head
for i in range(4):
	p.next = ListNode(i+2)
	p = p.next
p = head
while(p):
	print p.val
	p = p.next
s = Solution()
result = s.removeNthFromEnd(head,2)
p = result
while(p):
	print p.val
	p = p.next
