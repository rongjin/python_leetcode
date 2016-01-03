class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def rotateRight(self,head,k):
		if head == None:
			return None
		if k==0:
			return head
		p = head
		total = 0
		while(p):
			p = p.next
			total += 1
		print total
		k = k%total
		print k
		if k==0:
			return head
		p = head
		q = head
		i = 0
		while(i<k):
			p = p.next
			i+=1
		while(p.next):
			p = p.next
			q = q.next
		newhead = q.next
		p.next = head
		q.next = None
		return newhead

mylist = []
n = 5
for i in range(n):
	mylist.append(ListNode(i+1))
for i in range(n-1):
	mylist[i].next = mylist[i+1]
s = Solution()
newlist = s.rotateRight(mylist[0],5)
while(newlist):
	print newlist.val
	newlist = newlist.next
