class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
	
class Solution(object):
	def deleteDuplicates(self,head):
		if head==None:
			return head
		elif head.next == None:
			return head
		newhead = ListNode(-1)
		p = newhead
		q = head
		flag = 1
		while(q.next):
			print flag,q.val
			if q.val == q.next.val:
				flag = 0
			else:
				if flag == 1:
					p.next = q
					p = p.next
				else:
					flag = 1
			q = q.next
		if flag == 1:
			p.next = q
			p = p.next
		p.next = None
		return newhead.next

mylist = []
mylist.append(ListNode(1))
mylist.append(ListNode(3))
mylist.append(ListNode(3))
mylist.append(ListNode(5))
for i in range(3):
	mylist[i].next = mylist[i+1]
s = Solution()
newhead = s.deleteDuplicates(mylist[0])
while(newhead):
	print newhead.val
	newhead = newhead.next
