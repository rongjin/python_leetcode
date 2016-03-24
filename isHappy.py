class Solution(object):
	def isHappy(self,n):
		mydict = {}
		m = n
		while True:
			print m
			if m==1:
				return True
			elif m in mydict:
				return False
			else:
				mydict[m] = 1
				k = 0
				while(m>0):
					k+=(m%10)*(m%10)
					m/=10
				m = k

s = Solution()
print s.isHappy(19)
