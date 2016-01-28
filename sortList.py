#quick sort on linked list
class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def partition(self,head):
		h1 = ListNode(-1)
		h2 = ListNode(-1)
		p = h1
		q = h2
		h = head.next
		while(h):
			if h.val<head.val:
				p.next = h
				p = p.next
			else:
				q.next = h
				q = q.next
			h = h.next
		p.next = None
		q.next = None
		return h1.next,h2.next
	def check(self,head):
		p = head
		while(p and p.next):
			if p.val>p.next.val:
				return False
			p = p.next
		return True
	def sortList(self, head):
		if head == None:
			return None
		if head.next==None:
			return head
		if self.check(head):
			return head
		h1,h2= self.partition(head)
		if h1:
			if self.check(h1)==False:
				h1 = self.sortList(h1)
		if self.check(h2)==False:
			h2 = self.sortList(h2)
		if h1 == None:
			head.next = h2
			return head
		p = h1
		while(p.next):
			p = p.next
		p.next = head
		head.next = h2
		return h1

s = Solution()
l = [3,2,1]
mylist = []
for i in l:
	mylist.append(ListNode(i))
for i in range(len(l)-1):
	mylist[i].next = mylist[i+1]
result = s.sortList(mylist[0])
p = result
while(p):
	print p.val
	p = p.next
