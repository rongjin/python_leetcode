class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrderBottom(self,root):
		result = []
		if root == None:
			return result
		result.append([])
		queue = [root,None]
		while(queue):
			top = queue.pop(0)
			if top:
				print top.val
				result[-1].append(top.val)
				if top.left:
					queue.append(top.left)
				if top.right:
					queue.append(top.right)
			else:
				if result[-1] != []:
					result.append([])
					queue.append(None)
		result2 = []
		for i in range(1,len(result)):
			result2.append(result[len(result)-1-i])
		return result2

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c
print s.levelOrderBottom(a)
