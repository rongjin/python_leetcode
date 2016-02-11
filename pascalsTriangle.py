class Solution(object):
	def generate(self,numRows):
		result = []
		if numRows==0:
			return result
		result.append([1])
		if numRows == 1:
			return result
		result.append([1,1])
		if numRows == 2:
			return result
		for n in range(2,numRows):
			row = [1 for i in range(n+1)]
			for j in range(1,n):
				row[j]=result[-1][j-1]+result[-1][j]
			result.append(row)
		return result

s = Solution()
d = s.generate(5)
for i in d:
	print i

