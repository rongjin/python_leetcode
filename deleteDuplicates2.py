class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self,head):
		if head == None or head.next==None:
			return head
		p = head
		q = p.next
		while(p):
			q = p.next
			while(q and q.val==p.val):
				q = q.next
			p.next = q
			p = q
		return head

mylist = [1,1,2,3,3]
headlist = []
for i in mylist:
	headlist.append(ListNode(mylist[i]))
for i in range(len(mylist)-1):
	headlist[i].next = headlist[i+1]
s = Solution()
p = s.deleteDuplicates(headlist[0])
while(p):
	print p.val
	p = p.next
