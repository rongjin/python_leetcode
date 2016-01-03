class Solution(object):
	def get(self,matrix,i,h,l):
		top,bot,left,right = i,h-1-i,i,l-i-1
		mylist = []
		if top == bot:
			for j in range(left,right+1):
				mylist.append(matrix[top][j])
			return mylist
		elif left == right:
			for i in range(top,bot+1):
				mylist.append(matrix[i][left])
			return mylist
		else:
			mylist = [matrix[i][i]]
			cur = [i,i]
			while(True):
				if cur[0]==top:
					if cur[1]==right:
						cur[0]+=1
					else:
						cur[1]+=1
				elif cur[1]==right:
					if cur[0]==bot:
						cur[1]-=1
					else:
						cur[0]+=1
				elif cur[0]==bot:
					if cur[1]==left:
						cur[0]-=1
					else:
						cur[1]-=1
				else:
					cur[0]-=1
				if cur == [i,i]:
					break
				else:
					mylist.append(matrix[cur[0]][cur[1]])
			return mylist
	def spiralOrder(self,matrix):
		mylist = []
		h = len(matrix)
		if h==0:
			return mylist
		l = len(matrix[0])
		d = min(l,h)
		for i in range((d+1)/2):
			newlist = self.get(matrix,i,h,l)
			mylist += newlist
		return mylist

matrix = [[1,2,3],[4,5,6],[7,8,9]]
#matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
s = Solution()
print s.spiralOrder(matrix)
