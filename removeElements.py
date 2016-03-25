class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def removeElements(self,head,val):
		if head == None:
			return None
		newhead = ListNode(-1)
		newhead.next = head
		p = newhead
		while(p):
			q = p.next
			while(q and q.val==val):
				q = q.next
			p.next = q
			p = q
		return newhead.next

s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node1.next = node2
node2.next = node3
s2 = s.removeElements(node1,2)
p = s2
while(p):
	print p.val
	p = p.next
