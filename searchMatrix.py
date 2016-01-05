class Solution(object):
	def findrow(self,matrix,target,top,bot):
		if bot-top == 1:
			return top
		else:
			mid = (bot+top)/2
			val =  matrix[mid][0]
			if val == target:
				return mid
			elif val<target:
				return self.findrow(matrix,target,mid,bot)
			else:
				return self.findrow(matrix,target,top,mid)
	
	def findcol(self,row,target,left,right):
		print left,right
		if target<row[left]:
			return False
		elif target>row[right-1]:
			return False
		elif right-left == 1:
			if target == row[left]:
				return True
			else:
				return False
		else:
			mid = (left+right)/2
			if row[mid]==target:
				return True
			elif row[mid]>target:
				return self.findcol(row,target,left,mid)
			else:
				return self.findcol(row,target,mid,right)
	def searchMatrix(self,matrix,target):
		row = self.findrow(matrix,target,0,len(matrix))
		print row
		if row == -1:
			return False
		else:
			return self.findcol(matrix[row],target,0,len(matrix[row]))

s = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 11
matrix = [[1],[3],[5]]
target = 5
for i in matrix:
	print i
print
print s.searchMatrix(matrix,target)
