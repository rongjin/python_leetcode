class Solution(object):
	def check(self,cur,new):
		for i in range(len(cur)):
			if cur[i] == new:
				return False
			else:
				di = i-len(cur)
				dj = cur[i]-new
				if abs(di)==abs(dj):
					return False
		return True

	def totalNQueens(self,n):
		result = [[i] for i in range(n)]
		for i in range(1,n):
			for j in range(len(result)):
				cur = result.pop(0)
				for k in range(n):
					if self.check(cur,k):
						newlist = []
						for kk in cur:
							newlist.append(kk)
						newlist.append(k)
						result.append(newlist)
		return len(result)

s = Solution()
s.totalNQueens(4)

