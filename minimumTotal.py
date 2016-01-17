class Solution(object):
	def minimumTotal(self,triangle):
		if len(triangle)==1:
			return triangle[0][0]
		result = [0 for i in range(len(triangle))]
		result2 = [0 for i in range(len(triangle))]
		result[0] = triangle[0][0]
		print result
		for i in range(1,len(triangle)):
			print i
			for j in range(i+1):
				print triangle[i][j]
				if j==0:
					result2[j] = triangle[i][j]+result[j]
				elif j==i:
					result2[j]=triangle[i][j]+result[j-1]
				else:
					result2[j] = triangle[i][j]+min(result[j-1],result[j])
			print result2
			for i in range(len(result2)):
				result[i] = result2[i]
			mymin = 100000
		for i in range(len(triangle)):
			if result[i]<mymin:
				mymin = result[i]
		return mymin


triangle = []
triangle.append([2])
triangle.append([3,4])
triangle.append([6,5,7])
triangle.append([4,1,8,3])
s = Solution()
print s.minimumTotal(triangle)
