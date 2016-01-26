class RandomListNode(object):
	def __init__(self,x):
		self.label = x
		self.next = None
		self.random = None

class Solution(object):
	def copyRandomList(self, head):
		mydict = {}
		p = head
		newhead = RandomListNode(-1)
		q = newhead
		while(p!=None):
			if p not in mydict:
				newnode = RandomListNode(p.label)
				mydict[p] = newnode
				q.next = newnode
			else:
				q.next = mydict[p]
			q = q.next
			if p.random !=None:
				if p.random not in mydict:
					newnode2 = RandomListNode(p.random.label)
					mydict[p.random] = newnode2
					q.random = newnode2
				else:
					q.random = mydict[p.random]
			p = p.next
		for i in mydict:
			print i.label,mydict[i].label
		return newhead.next

mylist = []
for i in range(3):
	mylist.append(RandomListNode(i))
mylist[0].next = mylist[1]
mylist[1].next = mylist[2]
mylist[0].random = mylist[2]
s = Solution()
result = s.copyRandomList(mylist[0])
print
print result.label
print result.next.label
print result.random.label

