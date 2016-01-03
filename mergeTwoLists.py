class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self,l1,l2):
		pl1 = l1
		pl2 = l2
		head = ListNode(-1)
		p = head
		while(pl1!=None or pl2!=None):
			if pl1==None:
				p.next = pl2
				return head.next
			elif pl2==None:
				p.next = pl1
				return head.next
			else:
				if pl1.val<=pl2.val:
					p.next = pl1
					pl1 = pl1.next
					p = p.next
				else:
					p.next = pl2
					pl2 = pl2.next
					p = p.next
		return head.next

l1 = ListNode(0)
s = Solution()
l = s.mergeTwoLists(None,l1)
while(l):
	print l.val
	l = l.next
