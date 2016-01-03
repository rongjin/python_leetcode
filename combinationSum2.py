class Solution(object):
	def __init__(self):
		self.result = []
	def help(self,cand,target,cur):
		print cand,target,cur
		if target == 0:
			newcur = []
			for i in cur:
				newcur.append(i)
			self.result.append(newcur)
		elif cand == []:
			return
		else:
			i = 0;
			while(i<len(cand) and cand[i]<=target):
				cur.append(cand[i])
				self.help(cand[i+1:],target-cand[i],cur)
				cur.pop()
				i+=1
				while(i<len(cand) and cand[i]==cand[i-1]):
					i+=1
	def combinationSum2(self,candidates,target):
		cur = []
		candidates.sort()
		self.help(candidates,target,cur)
		return self.result

candidates = [10,1,2,7,6,1,5]
candidates = [2]
target = 8
target =1
s = Solution()
print s.combinationSum2(candidates,target)
