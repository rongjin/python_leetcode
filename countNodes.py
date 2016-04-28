class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def help(self,root,k,level,mylist):
			mylist[level] = 0
			p = root
			for i in range(1,k):
				if mylist[i] == 1:
					p = p.right
				else:
					p = p.left
			if p != None:
				mylist[level] = 1
			if k-1==level:
				result = 0
				for i in range(k):
					result = result*2+mylist[i]
				return result-1
			else:
				return self.help(root,k,level+1,mylist)
	def countNodes(self,root):
		if root==None:
			return 0
		p = root
		k = 1
		while(p.left):
			p = p.left
			k += 1
		k2 = 1
		p = root
		while(p.right):
			p = p.right
			k2 += 1
		if k == k2:
			result = 0
			for i in range(k):
				result = result*2+1
			return result
		mylist = [1 for i in range(k)]
		mylist[0] = 1
		count = self.help(root,k,1,mylist)
		return count

s = Solution()
nl = [TreeNode(0),TreeNode(1),TreeNode(2),TreeNode(3)]
nl[0].left = nl[1]
nl[0].right = nl[2]
nl[1].left = nl[3]
print s.countNodes(nl[0])

