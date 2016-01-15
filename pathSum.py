class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.result = []
	def help(self,root,sum,cur):
		if root != None:
			if root.left == None and root.right==None:
				if root.val==sum:
					newcur = [i for i in cur]
					newcur.append(root.val)
					self.result.append(newcur)
			else:
				cur.append(root.val)
				self.help(root.left,sum-root.val,cur)
				self.help(root.right,sum-root.val,cur)
				cur.pop()

	def pathSum(self,root,sum):
		if root == None:
			return []
		self.help(root,sum,[])
		return self.result

mylist = []
mylist.append(TreeNode(5))
mylist.append(TreeNode(4))
mylist.append(TreeNode(3))
mylist.append(TreeNode(1))
mylist[0].left = mylist[1]
mylist[0].right = mylist[2]
mylist[2].right = mylist[3]
s= Solution()
result = s.pathSum(mylist[0],9)
for i in result:
	print i
