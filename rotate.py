class Solution(object):
	def pos(self,l,i,j):
		pos1 = [i-l,j-l]
		pos2 = [pos1[1],-pos1[0]]
		pos3 = [-pos1[0],-pos1[1]]
		pos4 = [-pos1[1],pos1[0]]
		pos1[0] += l
		pos1[1] += l
		pos2[0] += l
		pos2[1] += l
		pos3[0] += l
		pos3[1] += l
		pos4[0] += l
		pos4[1] += l
		return pos1,pos2,pos3,pos4
	def help(self,matrix,i):
		print len(matrix)
		l = float(len(matrix)-1)/2
		print l
		for j in range(i,len(matrix)-i-1):
			pos1,pos2,pos3,pos4 = self.pos(l,i,j)
			print pos1,pos2,pos3,pos4
			temp = matrix[int(pos4[0])][int(pos4[1])]
			matrix[int(pos4[0])][int(pos4[1])] = matrix[int(pos3[0])][int(pos3[1])]
			matrix[int(pos3[0])][int(pos3[1])] = matrix[int(pos2[0])][int(pos2[1])]
			matrix[int(pos2[0])][int(pos2[1])] = matrix[int(pos1[0])][int(pos1[1])]
			matrix[int(pos1[0])][int(pos1[1])] = temp
	
	def rotate(self,matrix):
		l = (len(matrix)+1)/2
		for i in range(l):
			self.help(matrix,i)
		for i in matrix:
			print i
		print

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.rotate(mat)
