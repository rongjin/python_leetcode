class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def help(self,root,level,result):
		if level>=len(result):
			result.append([])
		if level%2==0:
			result[level].append(root.val)
		else:
			result[level].insert(0,root.val)
		if root.left:
			self.help(root.left,level+1,result)
		if root.right:
			self.help(root.right,level+1,result)
	def zigzagLevelOrder(self, root):
		if root == None:
			return []
		else:
			result = []
			self.help(root,0,result)
			print result
			return result

mylist = []
mylist.append(TreeNode(3))
mylist.append(TreeNode(9))
mylist.append(TreeNode(20))
mylist.append(TreeNode(15))
mylist.append(TreeNode(7))
mylist[0].left = mylist[1]
mylist[0].right = mylist[2]
mylist[2].left = mylist[3]
mylist[2].right = mylist[4]
s = Solution()
s.zigzagLevelOrder(mylist[0])
