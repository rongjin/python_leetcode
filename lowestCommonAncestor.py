class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.mymax = 0
		self.common = None

	def find(self,root,p,path):
		path.append(root)
		if(root!=p):
			if root.left:
				lfind = self.find(root.left,p,path)
				if lfind:
					return 1
			if root.right:
				rfind = self.find(root.right,p,path)
				if rfind:
					return 1
			path.pop()
			return 0
		else:
			return 1


	def lowestCommonAncestor(self,root,p,q):
		pathp = []
		pathq = []
		self.find(root,p,pathp)
		for i in pathp:
			print i.val,
		print
		self.find(root,q,pathq)
		for i in pathq:
			print i.val,
		print
		j = 0
		while(j<len(pathq) and j<len(pathp)):
			if pathp[j].val == pathq[j].val:
				j += 1
			else:
				break
		return pathp[j-1]

s = Solution()
nodelist = []
nodelist.append(TreeNode(6))
nodelist.append(TreeNode(2))
nodelist.append(TreeNode(8))
nodelist[0].left = nodelist[1]
nodelist[0].right = nodelist[2]
common = s.lowestCommonAncestor(nodelist[0],nodelist[1],nodelist[2])
print common.val
