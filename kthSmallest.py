class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def kthSmallest(self,root,k):
		#mid order traverse
		result = []
		mystack = []
		left = root
		l = 0
		while left:
			mystack.append(left)
			left = left.left
		print len(mystack)
		while(len(mystack)>0):
			top = mystack.pop()
			result.append(top.val)
			print result
			l += 1
			if l == k:
				return top.val
			if(top.right):
				left = top.right
				while(left):
					mystack.append(left)
					left = left.left


s = Solution()
nl = [TreeNode(1),TreeNode(2)]
nl[1].left = nl[0]
print s.kthSmallest(nl[1],1)

