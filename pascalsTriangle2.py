class Solution(object):
	def generate(self,rowIndex):
		numRows = rowIndex+1
		if numRows==0:
			return []
		if numRows == 1:
			return [1]
		if numRows == 2:
			return [1,1]
		result = [1 for i in range(numRows)]
		row = [1 for i in range(numRows)]
		result[0] = 1
		result[1] = 1
		for n in range(2,numRows):
			row = [1 for i in range(numRows)]
			for j in range(1,n):
				row[j]=result[j-1]+result[j]
			result = row
		return result

s = Solution()
d = s.generate(5)
print d

