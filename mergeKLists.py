from heapq import *

class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None
class Solution(object):
	def mergeKLists(self,lists):
		result = []
		k = len(lists)
		heap = []
		indexlist = []
		for i in range(k):
			indexlist.append(lists[i])
			if(lists[i]!=None):
				heappush(heap,(lists[i].val,i))
		print heap
		while(heap):
			root = heappop(heap)
			print root
			result.append(root[0])
			index = root[1]
			indexlist[index] = indexlist[index].next
			p = indexlist[index]
			if(p!=None):
				heappush(heap,(p.val,index))
			print heap
		print result

mlists = [[4,8,12],[1,5,9],[2,6,10],[3,7,11]]
#mlists = [[]]
lists = []
for i in mlists:
	head = ListNode(-1)
	p = head
	for j in range(len(i)):
		p.next = ListNode(i[j])
		p = p.next
	lists.append(head.next)
for i in lists:
	while(i):
		print i.val,
		i = i.next
	print

s = Solution()
s.mergeKLists(lists)
