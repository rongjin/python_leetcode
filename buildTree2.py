class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def help(self,inorder,postorder,il,ir,pl,pr):
		print il,ir,pl,pr
		if il==ir:
			return None
		elif ir-il==1:
			print inorder[il]
			return TreeNode(inorder[il])
		else:
			i = 1
			while(ir-i>il and inorder[ir-i]!=postorder[pr-1]):
				i+=1
			print i
			root = TreeNode(postorder[pr-1])
			left = self.help(inorder,postorder,il,ir-i,pl,pr-i)
			right = self.help(inorder,postorder,ir-i+1,ir,pr-i,pr-1)
			root.left = left
			root.right = right
			return root
	def buildTree(self,inorder,postorder):
		root = self.help(inorder,postorder,0,len(inorder),0,len(postorder))
		return root
s = Solution()
inorder = [2,3,1]
postorder = [3,2,1]
result = s.buildTree(inorder,postorder)
print result.val
#print result.left.val
#print result.right.val
