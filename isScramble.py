class Solution(object):
	def isScramble(self,s1,s2):
		print s1,s2
		if s1 == s2:
			return True
		elif sorted(s1)!=sorted(s2):
			return False
		else:
			for l in range(1,len(s1)):
				l1 = l
				l2 = len(s1)-l
				if self.isScramble(s1[:l1],s2[:l1]) and \
						self.isScramble(s1[l1:],s2[l1:]):
					return True
				elif self.isScramble(s1[:l1],s2[l2:]) and\
						self.isScramble(s1[l1:],s2[:l2]):
					return True
			return False
s1 = "rgtae"
s2 = "great"
s = Solution()
print s.isScramble(s1,s2)
