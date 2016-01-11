class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
	
class Solution(object):
	def help(self,head):
		if head.next == None:
			return head
		else:
			revhead = head.next
			rev = self.help(revhead)
			revhead.next = head
			head.next = None
			return rev
	def reverseBetween(self,head,m,n):
		newhead = ListNode(-1)
		newhead.next = head
		p = newhead
		pcount = 1
		while(pcount<m):
			pcount+=1
			p = p.next
		q = newhead
		qcount = 0
		while(qcount<n):
			qcount+=1
			q = q.next
		last = q.next
		q.next = None
		#print p.val,q.val
		revhead = p.next
		rev = self.help(revhead)#rev is the head
		p.next = rev
		revhead.next = last
		return(newhead.next)

s = Solution()
mylist = []
for i in range(5):
	mylist.append(ListNode(i+1))
for i in range(4):
	mylist[i].next=mylist[i+1]
#newlist = s.help(mylist[0])
newlist = s.reverseBetween(mylist[0],1,5)
p = newlist
while(p):
	print p.val
	p = p.next
