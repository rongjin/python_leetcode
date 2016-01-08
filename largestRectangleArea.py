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
			print i,mystack
			if mystack == [] or height[i]>=height[mystack[-1]]:
				mystack.append(i)
			else:
				l = mystack.pop()
				h = height[l]
				while(h>height[i]):
					print mystack[-1],i,h
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
		return largest

height = [2,1,5,6,2,3]
#height = [2,1,2]
s = Solution()
print s.largestRectangleArea(height)
