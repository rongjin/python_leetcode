class Solution(object):
	def __init__(self):
		self.result = []
	def help(self,cand,target,cur):
		print cand,target,cur
		if target==0:
			newcur = []
			for i in cur:
				newcur.append(i)
			self.result.append(newcur)
			print "find",self.result
		elif cand == []:
			return
		else:
			i = 0
			while(i<len(cand) and cand[i]<=target):
				cur.append(cand[i])
				self.help(cand[i:],target-cand[i],cur)
				cur.pop()
				i+=1
	def combinationSum(self,candidates,target):
		cur = []
		candidates.sort()
		self.help(candidates,target,cur)
		return self.result
s = Solution()
cand = [2,3,6,7]
target = 7
print s.combinationSum(cand,target)
