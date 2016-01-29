class ListNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return
        head2 = self.findMid(head)
        head2 = self.reverseList(head2)
        self.zigZagMerge(head, head2)
    
    def findMid(self, head):
        slow, fast = head, head.next
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        head2, slow.next = slow.next, None
        return head2
    
    def reverseList(self, head):
        pre, cur = head, head.next
        while cur:
            tmp, cur.next = cur.next, pre
            pre, cur = cur, tmp
        head.next = None
        return pre
    
    def zigZagMerge(self, head, head2):
        cur1, cur2 = head, head2
        while cur2:
            tmp1, tmp2 = cur1.next, cur2.next
            cur1.next, cur2.next = cur2, tmp1
            cur1, cur2 = tmp1, tmp2

s = Solution()
mylist = [3,2,3,3,3,1,3,1,3,3,1,1,3,3,2,1,1,1,1,2,1,1,2,1,2,1,3,2,3,1,1,1,2,2,3,3,1,3,1,2,2,2,3,3,2,3,3,1,1,3,1,3,2,2,1,2,1,1,2,3,2,1,3,2,3,1,2,2,2,2,2,3,1,2,2,3,1,2,3,3,1,1,3,2,2,2,2,2,3,3,2,1,2,2,3,2,2,2,1,3,2,3,2,1,3,2,3,3,3,3,2,3,3,3,1,1,2,2,2,3,3,1,2,3,1,2,2,3,1,2,1,1,2,3,2,1,2,1,3,1,1,3,2,2,1,1,3,2,2,1,2,2,1,2,2,1,1,3,3,1,3,1,2,2,1,1,1,3,2,1,3,3,2,3,1,1,2,2,1,1,3,1,1,1,2,2,1,3,1,3,1,1,3,2,1,1,1,2,2,2,1,3,3,1,3,2,2,2,3,3,2,3,2,3,1,2,2,2,2,3,1,3,2,1,2,2,2,2,3,2,1,2,1,1,3,1,3,1,3,2,3,1,2,1,3,2,3,2,3,1,2,2,2,2,1,2,2,3,2,3,1,1,1,2,1,2,2,1,2,1,1,3,3,1,3,3,3,3,1,3,1,3,3,1,2,3,2,1,1,1,3,3,1,1,1,2,2,3,1,1,2,3,2,3,1,2,1,3,3,3,1,2,2,3,1,2,2,3,3,2,2,1,1,1,3,2,3,3,3,3,3,1,3,1,2,3,1,3,1,1,1,2,3,1,1,1,1,2,1,2,3,2,3,2,1,1,2,3,2,1,3,1,3,2,1,3,1,1,3,3,2,2,2,2,2,2,1,2,3,1,3,2,2,3,3,2,2,3,1,3,3,1,1,3,2,1,2,1]
listlist = []
for i in mylist:
	listlist.append(ListNode(i))
for i in range(len(mylist)-1):
	listlist[i].next = listlist[i+1]
s.reorderList(listlist[0])
p = listlist[0]
print
while p:
	print p.val
	p = p.next
