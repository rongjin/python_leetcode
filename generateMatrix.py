class Solution(object):
	def setmat(self,n,mat,i,begin):
		cur = [i,i]
		mat[cur[0]][cur[1]] = begin
		begin += 1
		cur[1]+=1
		left = i
		right = n-1-i
		top = i
		bot = n-1-i
		if top == bot:
			return begin
		while(cur!=[i,i]):
			mat[cur[0]][cur[1]]=begin
			if cur[0] == top:
				if cur[1] == right:
					cur[0]+=1
				else:
					cur[1]+=1
			elif cur[1]==right:
				if cur[0] == bot:
					cur[1]-=1
				else:
					cur[0]+=1
			elif cur[0] == bot:
				if cur[1]==left:
					cur[0]-=1
				else:
					cur[1]-=1
			elif cur[1] == left:
				cur[0]-=1
			begin += 1
		return begin
	def generateMatrix(self,n):
		l = (n+1)/2
		mat = [[0 for i in range(n)] for i in range(n)]
		begin = 1
		for i in range(l):
			begin = self.setmat(n,mat,i,begin)
		return mat

s = Solution()
mat = s.generateMatrix(6)
for i in mat:
	print i
