class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):

	def swapPairs(self,head):
		if head == None:
			return head
		elif head.next == None:
			return head
		else:
			newhead = head.next
			p = newhead
			q = head.next.next
			p.next = head
			head.next = self.swapPairs(q)
			return(newhead)


mylist = [1,2,3]
head = ListNode(-1)
p = head
for i in mylist:
	p.next = ListNode(i)
	p = p.next
s = Solution()
newhead = s.swapPairs(head.next)
while(newhead):
	print newhead.val
	newhead = newhead.next
