class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
	def insertionSortList(self,head):
		newhead = ListNode(-100000)
		q = newhead
		p = head
		while(p):
			if p.val>=q.val:
				temp = p.next
				q.next = p
				p.next = None
				p = temp
				q = q.next
			else:
				p2 = newhead
				while(p2.next and p2.next.val<p.val):
					p2 = p2.next
				temp = p.next
				temp_p2 = p2.next
				p2.next = p
				p.next = temp_p2
				p = temp
		return newhead.next

l = [-84,142,41,-17,-71,170,186,183,-21,-76,76,10,29,81,112,-39,-6,-43,58,41,111,33,69,97,-38,82,-44,-7,99,135,42,150,149,-21,-30,164,153,92,180,-61,99,-81,147,109,34,98,14,178,105,5,43,46,40,-37,23,16,123,-53,34,192,-73,94,39,96,115,88,-31,-96,106,131,64,189,-91,-34,-56,-22,105,104,22,-31,-43,90,96,65,-85,184,85,90,118,152,-31,161,22,104,-85,160,120,-31,144,115]
mylist = []
for i in l:
	mylist.append(ListNode(i))
for i in range(len(l)-1):
	mylist[i].next = mylist[i+1]
s = Solution()
result = s.insertionSortList(mylist[0])
p = result
while(p):
	print p.val
	p = p.next
