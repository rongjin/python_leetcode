class Solution(object):
	def help(self,s,num):
		if num*3<len(s):
			return []
		if len(s)==0:
			return []
		if num == 1:
			if len(s)>1 and s[0]=="0":
				return []
			if int(s)>=0 and int(s)<=255:
				return [s]
			else:
				return []
		else:
			newresult = []
			for i in range(3):
				first = s[:(i+1)]
				if len(first)>1 and first[0]=="0":
					continue
				elif int(first)>=0 and int(first)<=255:
					result = self.help(s[i+1:],num-1)
					for j in result:
						ll = first+"."+j
						newresult.append(ll)
			return newresult
					
	def restoreIpAddresses(self,s):
		result = self.help(s,4)
		return result

mystr = "25525511105"
#mystr = "0000"
s = Solution()
newresult = s.restoreIpAddresses(mystr)
print newresult
