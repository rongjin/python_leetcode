class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def hasCycle(self,head):
		p = head
		q = head
		while(q and q.next):
			p = p.next
			q = q.next.next
			if q==p:
				return True
		return False

s = Solution()
mylist = []
mylist.append(ListNode(1))
mylist[0].next = mylist[0]
print s.hasCycle(mylist[0])

