class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def detectCycle(self,head):
		i = 0
		p = head
		q = head
		find = 0
		while(q and q.next):
			q = q.next.next
			p = p.next
			i+=1
			if p==q:
				find = 1
				break
		if find ==0:
			return None
		q = head
		print i
		j = 0
		while(j<i):
			q = q.next
			j+=1
		p = head
		while(p!=q):
			p = p.next
			q = q.next
		return p

mylist = []
for i in range(8):
	mylist.append(ListNode(i))
for i in range(7):
	mylist[i].next = mylist[i+1]
mylist[7].next = mylist[2]
s = Solution()
first = s.detectCycle(mylist[0])
print first.val
