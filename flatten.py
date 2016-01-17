class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None
    
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root

mylist = []
mylist.append(TreeNode(1))
mylist.append(TreeNode(2))
mylist.append(TreeNode(5))
mylist[0].left= mylist[1]
mylist[0].right= mylist[2]
s = Solution()
s.flatten(mylist[0])
print
print mylist[0].right.val
print mylist[1].right.val
