class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sortedArrayToBST(self,nums):
		l = len(nums)
		if l==0:
			return None
		elif l==1:
			return TreeNode(nums[0])
		else:
			mid = l/2
			root = TreeNode(nums[mid])
			left = self.sortedArrayToBST(nums[:mid])
			right = self.sortedArrayToBST(nums[mid+1:])
			root.left = left
			root.right = right
			return root

s = Solution()
nums = [1,2,3]
result = s.sortedArrayToBST(nums)
print result.val
print result.left.val
print result.right.val

