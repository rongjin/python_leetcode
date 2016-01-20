class Solution(object):
	def find(self,mydict,n):
		d = mydict[n]
		if d[0]==None:
			return n,d[1]
		while mydict[d[0]][0]!=None:
			d = mydict[d[0]]
		d2 = mydict[d[0]]
		return d[0],d2[1]
	def update(self,mydict,a,b):
		pa,ha = self.find(mydict,a)
		print a,pa,ha
		pb,hb = self.find(mydict,b)
		print b,pb,hb
		if ha>=hb:
			mydict[pb][0] = pa
			mydict[pa][1] = ha+hb
		else:
			mydict[pa][0] = pb
			mydict[pb][1] = ha+hb
	def longestConsecutive(self,nums):
		mydict = {}
		for n in nums:
			if n in mydict:
				continue
			mydict[n] = [None,1]#parent,height
			if n-1 in mydict:
				print "con",n-1,n
				self.update(mydict,n-1,n)
				print mydict
			if n+1 in mydict:
				print "con",n+1,n
				self.update(mydict,n+1,n)
				print mydict
		longest = 0
		for i in mydict.keys():
			if mydict[i][0]==None:
				if mydict[i][1]>longest:
					longest = mydict[i][1]
		return longest


nums = [1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]
nums = [100,4,2,1,3]
print nums
s = Solution()
print s.longestConsecutive(nums)
