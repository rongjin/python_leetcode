class Solution(object):
	def trap(self,height):
		mysum = 0
		mystack = []
		i = 0
		left = 0
		while(i<len(height)):
			if mystack == [] or height[i]<left:
				mystack.append(height[i])
				if height[i]>left:
					left = height[i]
				i+=1
				print mystack
			elif height[i]>=left:
				h = mystack.pop()
				while(h<=left):
					mysum += (left-h)
					if mystack == []:
						break
					h = mystack.pop()
				left = height[i]
				mystack.append(height[i])
				print mystack
				i+=1
		print mysum
		mystack2 = []
		right = 0
		while(len(mystack)!=0):
			top = mystack.pop()
			if mystack2 == [] or top < right:
				mystack2.append(top)
				if top>right:
					right = top
				print mystack2
			else:
				h = mystack2.pop()
				while(h<=right):
					mysum += right-h
					if mystack2 == []:
						break
					h = mystack2.pop()
				right = top
				mystack2.append(top)
				print mystack2
		print mysum
		return mysum

s = Solution()
height = [0,1,0,2,1,0,1,2,2,1,2,1]
height = [2,0,2]
print s.trap(height)
