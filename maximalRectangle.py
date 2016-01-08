class Solution(object):
	def largestRectangleArea(self,height):
		if height == []:
			return 0
		elif len(height)==1:
			return height[0]
		largest = 0
		height.insert(0,0)
		height.append(0)
		mystack = []
		i = 0
		while(i<len(height)):
			#print i,mystack
			if mystack == [] or height[i]>=height[mystack[-1]]:
				mystack.append(i)
			else:
				l = mystack.pop()
				h = height[l]
				while(h>height[i]):
					#print mystack[-1],i,h
					area = (i-mystack[-1]-1)*h
					if area>largest:
						largest = area
					if mystack != [] and height[i]<height[mystack[-1]]:
						l = mystack.pop()
						h = height[l]
					else:
						break
				mystack.append(i)
			i+=1
		del height[0]
		del height[-1]
		return largest
	
	def maximalRectangle(self,matrix):
		if len(matrix)==0:
			return 0
		else:
			largest = 0
			height = [0 for i in range(len(matrix[0]))]
			for i in range(len(matrix)):
				for j in range(len(matrix[0])):
					if matrix[i][j]=="0":
						height[j] = 0
					else:
						height[j]+=1
				print height
				lar = self.largestRectangleArea(height)
				if lar>largest:
					largest = lar
			return largest

mat = [[1,1],[0,1]]
#height = [2,1,2]
s = Solution()
print s.maximalRectangle(mat)
