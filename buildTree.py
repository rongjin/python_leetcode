class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def help(self,preorder,inorder,pl,pr,il,ir):
		print pl,pr,il,ir
		if pr == pl:
			return None
		elif pr-pl==1:
			return TreeNode(preorder[pl])
		else:
			root = TreeNode(preorder[pl])
			i = 0
			while(i+il<ir and inorder[i+il]!=root.val):
				i += 1
			print i
			left = self.help(preorder,inorder,pl+1,pl+i+1,il,il+i)
			right = self.help(preorder,inorder,pl+i+1,pr,il+i+1,ir)
			root.left = left
			root.right = right
			return root
	def buildTree(self,preorder,inorder):
		root = self.help(preorder,inorder,0,len(preorder),0,len(inorder))
		return root

pre = [4,2,1,3]
inorder = [1,2,3,4]
s = Solution()
result = s.buildTree(pre,inorder)
print result.val
print result.left.val
print result.right.val


