class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
	
class Solution(object):
	def help(self,root):
		print root.val
		if root.left==None and root.right==None:
			result= 1,root.val,root.val
		elif root.left==None:
			rcheck,rmin,rmax = self.help(root.right)
			if rcheck == 0 or rmin<=root.val:
				result= 0,0,0
			else:
				result= 1,root.val,rmax
		elif root.right==None:
			lcheck,lmin,lmax = self.help(root.left)
			if lcheck==0 or lmax >= root.val:
				result= 0,0,0
			else:
				result= 1,lmin,root.val
		else:
			lcheck,lmin,lmax = self.help(root.left)
			if lcheck==0:
				result= 0,0,0
			rcheck,rmin,rmax = self.help(root.right)
			if rcheck==0:
				result= 0,0,0
			elif lmax < root.val and rmin>root.val:
				result= 1,lmin,rmax
			else:
				result= 0,lmin,rmax
		print result
		return result
	def isValidBST(self,root):
		if root == None:
			return True
		result = self.help(root)
		if result[0] == 0:
			return False
		else:
			return True

s = Solution()
mylist = []
mylist.append(TreeNode(1))
mylist.append(TreeNode(1))
mylist[0].left = mylist[1]
print s.isValidBST(mylist[0])
		
